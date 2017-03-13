# imports - compatibility packages
from __future__ import absolute_import

# imports - third-party packages
import numpy as np

# module imports
from bulbea._utils import _check_type, _check_int, _check_real, _check_iterable
import bulbea as bb

def _normalize(data):
    normalized = np.array([ ((sample / sample[0]) - 1)for sample in data ])
    return normalized

def split(share,
          attr      = 'Close',
          window    = 0.01,
          train     = 0.60,
          shift     = 1,
          normalize = False):
    '''
    :param attrs: `str` or `list` of attribute names of a share, defaults to *Close* attribute
    :type attrs: :obj: `str`, :obj:`list`
    '''
    _check_type(share, type_ = bb.Share, raise_err = True, expected_type_name = 'bulbea.Share')
    _check_iterable(attrs, raise_err = True)
    _check_int(shift, raise_err = True)
    _check_real(window, raise_err = True)
    _check_real(train, raise_err = True)

    _check_in_range(window, 0, 1, raise_err = True)
    _check_in_range(train, 0, 1, raise_err = True)

    data   = share.data[attribute]
    length = len(share)

    window = int(np.rint(length * window))
    offset = shift - 1

    splits = np.array([data[i if i is 0 else i + offset: i + window] for i in range(length - window)])

    if normalize:
        splits = _normalize(splits)

    size   = len(splits)
    split  = int(np.rint(train * size))

    train  = splits[:split,:]
    test   = splits[split:,:]

    Xtrain, Xtest = train[:,:-1], test[:,:-1]
    ytrain, ytest = train[:, -1], test[:, -1]

    return (Xtrain, Xtest, ytrain, ytest)
