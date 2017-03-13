# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
import matplotlib.pyplot as pplt
import quandl

# module imports
from bulbea.config.app import AppConfig
from bulbea.entity import Entity
from bulbea._util import _check_str, _check_int, _check_pandas_series, _check_iterable, _assign_if_none, _get_type_name, _raise_type_error

pplt.style.use(AppConfig.PLOT_STYLE)

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
    A user-created :class:`Share <Share>` object.

    :param source: *source* symbol for economic data
    :type source: :obj:`str`

    :param ticker: *ticker* symbol of a share
    :type ticker: :obj:`str`

    :Example:

    >>> import bulbea as bb
    >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
    >>> share.data.sample(1)
                Open       High        Low  Close      Volume  Adjusted Close
    Date
    2003-05-15  18.6  18.849999  18.470001  18.73  71248800.0        1.213325
    '''
    def __init__(self, source, ticker):

        _check_str(source, raise_err = True)
        _check_str(ticker, raise_err = True)

        self.source  = source
        self.ticker  = ticker

        self._update()

    def update(self):
        '''
        Update the share with the latest available data.

        :Example:

        >>> import bulbea as bb
        >>> share = bb.Share(source = 'YAHOO', ticker = 'AAPL')
        >>> share.update()
        '''
        self._update()

    def _update(self):
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
