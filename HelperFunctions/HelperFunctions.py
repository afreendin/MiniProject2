import statistics as stat
from scipy import stats
from scipy.stats.stats import pearsonr
import numpy as np


class HelperFunctions:

    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = float(a) + float(b)
        return self.result

    def subtract(self, a, b):
        self.result = float(a) - float(b)
        return self.result

    def multiply(self, a, b):
        self.result = float(a) * float(b)
        return self.result

    def division(self, a, b):
        self.result = float(a) / float(b)
        return self.result

    def square(self, a):
        self.result = float(a)**2;
        return self.result

    def square_root(self, a):
        self.result = float(a)**(1/2.0)
        return self.result

    # Library functions

    def mean(self, data):
        self.result = stat.mean(data)
        return "{0:.2f}".format(round(self.result, 2))

    def median(self, data):
        self.result = stat.median(data)
        return "{0:.2f}".format(round(self.result, 2))

    def mode(self, data):
        self.result = stat.mode(data)
        return self.result

    def variance(self, data):
        self.result = stat.variance(data)
        return "{0:.2f}".format(round(self.result, 2))

    def standard_deviation(self, data):
        self.result = stat.stdev(data)
        return "{0:.2f}".format(round(self.result, 2))

    def skewness(self, data):
        skew = 3*(float(self.mean(data)) - float(self.median(data)))/float(self.standard_deviation(data))
        return "{0:.2f}".format(round(skew, 2))

    def sample_correlation(self, datax, datay):
        corr = pearsonr(datax, datay)
        return  corr

    def z_score(self, datax):
        zscore = stats.zscore(datax)
        zscore = ["%.2f"%item for item in zscore]
        return [float(k) for k in zscore]