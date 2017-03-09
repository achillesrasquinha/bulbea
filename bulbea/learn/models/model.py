from six import with_metaclass

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
