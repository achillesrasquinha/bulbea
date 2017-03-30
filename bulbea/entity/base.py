# imports - compatibility imports
from six import with_metaclass

# imports - standard imports
from abc import ABCMeta

class Entity(with_metaclass(ABCMeta)):
    '''
    A base class for an entity object.
    '''
    pass
