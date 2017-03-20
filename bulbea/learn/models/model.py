# imports - compatibility imports
from six import with_metaclass

# imports - standard imports
from abc import ABCMeta, abstractmethod

class Model(with_metaclass(ABCMeta)):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

class Supervised(Model):
    def fit(self, X, y):
        pass

    def predict(self, X):
        pass

class UnSupervised(Model):
    def fit(self, X, y = None):
        pass

    def predict(self, X):
        pass

class Classifier(Supervised):
    pass

class Regressor(Supervised):
    pass