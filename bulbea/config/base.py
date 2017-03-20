# imports - compatibility imports
from six import with_metaclass

# imports - standard imports
from abc import ABCMeta

class BaseConfig(with_metaclass(ABCMeta)):
    pass
