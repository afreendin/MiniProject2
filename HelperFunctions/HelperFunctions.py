import statistics as stat
from scipy import stats
from scipy.stats.stats import pearsonr
import numpy as np


# class HelperFunctions:
#
#     result = 0.0

# def __init__(self):
#     pass


def add(a, b):
    result = float(a) + float(b)
    return result


def subtract(a, b):
    result = float(a) - float(b)
    return result


def multiply(a, b):
    result = float(a) * float(b)
    return result


def division(a, b):
    result = float(a) / float(b)
    return result


def square(a):
    result = float(a)**2
    return result


def square_root(a):
    result = float(a)**(1/2.0)
    return result


# def add(self, a, b):
#     self.result = float(a) + float(b)
#     return self.result
#
# def subtract(self, a, b):
#     self.result = float(a) - float(b)
#     return self.result
#
# def multiply(self, a, b):
#     self.result = float(a) * float(b)
#     return self.result
#
# def division(self, a, b):
#     self.result = float(a) / float(b)
#     return self.result
#
# def square(self, a):
#     self.result = float(a)**2;
#     return self.result
#
# def square_root(self, a):
#     self.result = float(a)**(1/2.0)
#     return self.result


# Library functions


def lib_mean(data):
    result = stat.mean(data)
    return "{0:.2f}".format(round(result, 2))


def lib_median(data):
    result = stat.median(data)
    return "{0:.2f}".format(round(result, 2))


def lib_mode(data):
    result = stat.mode(data)
    return result


def lib_variance(data):
    result = stat.variance(data)
    return "{0:.2f}".format(round(result, 2))


def lib_standard_deviation(data):
    result = stat.stdev(data)
    return "{0:.2f}".format(round(result, 2))


def lib_skewness(data):
    skew = 3*(float(lib_mean(data)) - float(lib_median(data)))/float(lib_standard_deviation(data))
    return "{0:.2f}".format(round(skew, 2))


def lib_sample_correlation(datax, datay):
    corr = pearsonr(datax, datay)
    return corr


def lib_zscore(datax):
    zscore = stats.zscore(datax)
    zscore = ["%.2f"%item for item in zscore]
    return [float(k) for k in zscore]


# def mean(self, data):
#     self.result = stat.mean(data)
#     return "{0:.2f}".format(round(self.result, 2))
#
# def median(self, data):
#     self.result = stat.median(data)
#     return "{0:.2f}".format(round(self.result, 2))
#
# def mode(self, data):
#     self.result = stat.mode(data)
#     return self.result
#
# def variance(self, data):
#     self.result = stat.variance(data)
#     return "{0:.2f}".format(round(self.result, 2))
#
# def standard_deviation(self, data):
#     self.result = stat.stdev(data)
#     return "{0:.2f}".format(round(self.result, 2))
#
# def skewness(self, data):
#     skew = 3*(float(self.mean(data)) - float(self.median(data)))/float(self.standard_deviation(data))
#     return "{0:.2f}".format(round(skew, 2))
#
# def sample_correlation(self, datax, datay):
#     corr = pearsonr(datax, datay)
#     return  corr
#
# def z_score(self, datax):
#     zscore = stats.zscore(datax)
#     zscore = ["%.2f"%item for item in zscore]
#     return [float(k) for k in zscore]
#
