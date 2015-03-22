__author__ = 'tampe125'

from abc import ABCMeta, abstractmethod


class AbstractDetector():
    __metaclass__ = ABCMeta

    score = 0
    data  = ''
    lines = 0

    def reset(self):
        self.score = 0
        self.data  = ''

        return self

    def setinfo(self, features):
        for feature, value in features.iteritems():
            setattr(self, feature, value)

        return self

    @abstractmethod
    def analyze(self, results):
        pass

    @abstractmethod
    def returnkey(self):
        pass