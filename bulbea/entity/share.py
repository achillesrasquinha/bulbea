# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
import matplotlib.pyplot as pplt
import pandas as pd
import quandl

# module imports
from bulbea.config.app import AppConfig
from bulbea.entity import Entity
from bulbea._util import (
    _check_str,
    _check_int,
    _check_pandas_series,
    _check_pandas_dataframe,
    _check_iterable,
    _assign_if_none,
    _get_type_name,
    _raise_type_error,
    _is_sequence_all
)

pplt.style.use(AppConfig.PLOT_STYLE)

def _get_cummulative_return(data):
    cumret = (data / data[0]) - 1

    return cumret

def _get_bollinger_bands_columns(data):
    _check_pandas_dataframe(data, raise_err = True)

    columns   = list(data.columns)
    ncols     =  len(columns)

    if ncols != 3:
        raise ValueError('Expected a pandas.DataFrame with exactly 3 columns, got {ncols} instead.'.format(
            ncols = ncols
        ))

    if not _is_sequence_all(columns):
        raise ValueError('Ambiguous column names: {columns}'.format(
            columns = columns
        ))

    attr       = columns[0]
    prefixes   = ['Lower', 'Mean', 'Upper']
    columns    = ['{prefix} ({attr})'.format(
        prefix = prefix,
        attr   = attr
    ) for prefix in prefixes]

    return columns

def _get_bollinger_bands(data, period = 50, bandwidth = 1):
    _check_int(period,    raise_err = True)
    _check_int(bandwidth, raise_err = True)

    _check_pandas_series(data, raise_err = True)

    roll      = data.rolling(window = period)
    std, mean = roll.std(), roll.mean()

    upper     = mean + bandwidth * std
    lower     = mean - bandwidth * std

    return (lower, mean, upper)

def _plot_global_mean(data, axes):
    _check_pandas_series(data, raise_err = True)

    mean     = data.mean()
    axes.axhline(mean, color = 'b', linestyle = '-.')

def _plot_bollinger_bands(data, axes, period = 50, bandwidth = 1):
    _check_int(period,    raise_err = True)
    _check_int(bandwidth, raise_err = True)

    _check_pandas_series(data, raise_err = True)

    lowr, mean, uppr = _get_bollinger_bands(data, period = period, bandwidth = bandwidth)

    axes.plot(lowr, color = 'r', linestyle = '--')
    axes.plot(mean, color = 'g', linestyle = '--')
    axes.plot(uppr, color = 'r', linestyle = '--')

class Share(Entity):
    '''
    A user-created :class:`Share <bulbea.Share>` object.

    :param source: *source* symbol for economic data
    :type source: :obj:`str`

    :param ticker: *ticker* symbol of a share
    :type ticker: :obj:`str`

    :Example:

    >>> import bulbea as bb
    >>> share = bb.Share(source = 'YAHOO', ticker = 'GOOGL')
    >>> share.data.sample(1)
                Open       High        Low  Close      Volume  Adjusted Close
    Date
    2003-05-15  18.6  18.849999  18.470001  18.73  71248800.0        1.213325
    '''
    def __init__(self, source, ticker, start = None, end = None, latest = None):
        _check_str(source, raise_err = True)
        _check_str(ticker, raise_err = True)

        self.source  = source
        self.ticker  = ticker

        self._update(start = start, end = end, latest = latest)

    def update(self):
        '''
        Update the share with the latest available data.

        :Example:

        >>> import bulbea as bb
        >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
        >>> share.update()
        '''
        self._update()

    def _update(self, start = None, end = None, latest = None):
        self.data    = quandl.get('{database}/{code}'.format(
            database = self.source,
            code     = self.ticker
        ))
        self.length  =  len(self.data)
        self.attrs   = list(self.data.columns)

    def __len__(self):
        '''
        Number of data points available for a given share.

        :Example:
        >>> import bulbea as bb
        >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
        >>> len(share)
        9139
        '''
        return self.length

    def bollinger_bands(self,
                        attrs     = 'Close',
                        period    = 50,
                        bandwidth = 1):
        '''
        Bollinger Bands for each attribute.

        :param attrs: `str` or `list` of attribute names of a share to plot, defaults to *Close* attribute
        :type attrs: :obj: `str`, :obj:`list`



        :Example:

        >>> import bulbea as bb
        >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
        >>> data  = share.bollinger_bands()
        >>> data.tail()
                    Lower (Close)  Mean (Close)  Upper (Close)
        Date
        2017-03-07     815.145883    831.694803     848.243724
        2017-03-08     816.050821    832.574004     849.097187
        2017-03-09     817.067353    833.574805     850.082257
        2017-03-10     817.996674    834.604404     851.212135
        2017-03-13     819.243360    835.804605     852.365849
        '''
        _check_iterable(attrs, raise_err = True)

        if _check_str(attrs):
            attrs = [attrs]

        frames = list()

        for attr in attrs:
            data                    = self.data[attr]
            lowr, mean, upper       = _get_bollinger_bands(data, period = period, bandwidth = bandwidth)
            bollinger_bands         = pd.concat([lowr, mean, upper], axis = 1)
            bollinger_bands.columns = _get_bollinger_bands_columns(bollinger_bands)

            frames.append(bollinger_bands)

        return frames[0] if len(frames) == 1 else frames

    def plot(self,
             attrs           = 'Close',
             global_mean     = False,
             bollinger_bands = False,
             period          = 50,
             bandwidth       = 1,
             subplots        = False, *args, **kwargs):
        '''
        :param attrs: `str` or `list` of attribute names of a share to plot, defaults to *Close* attribute
        :type attrs: :obj: `str`, :obj:`list`

        :Example:

        >>> import bulbea as bb
        >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
        >>> share.plot()
        '''
        _check_iterable(attrs, raise_err = True)

        if _check_str(attrs):
            attrs  = [attrs]

        plot_stats = global_mean or bollinger_bands
        subplots   = True if len(attrs) != 1 and plot_stats else subplots
        axes       = self.data[attrs].plot(subplots = subplots, *args, **kwargs)

        if plot_stats:
            if subplots:
                for i, attr in enumerate(attrs):
                    data = self.data[attr]
                    ax   = axes[i]

                    if global_mean:
                        _plot_global_mean(data, ax)

                    if bollinger_bands:
                        _plot_bollinger_bands(data, ax, period = period, bandwidth = bandwidth)
            else:
                attr = attrs[0]
                data = self.data[attr]

                if global_mean:
                    _plot_global_mean(data, axes)

                if bollinger_bands:
                    _plot_bollinger_bands(data, axes, period = period, bandwidth = bandwidth)

        return axes
