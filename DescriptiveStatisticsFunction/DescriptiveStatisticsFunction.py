import sys
sys.path.append('../HelperFunctions')
from HelperFunctions import HelperFunctions
import statistics as stat
import numpy as np


class DescriptiveStatisticsFunction:

    result = 0.0

    def __init__(self):
        self.calc = HelperFunctions
        pass

    def mean(self, data):
        total = 0.0
        for k in range(len(data)):
            total = self.calc.add(total, data[k])
            self.result = self.calc.division(total, len(data))

        return "{0:.2f}".format(round(self.result,2))

    def median(self, data):
        count = len(data)
        sort = sorted(data)
        med_pos = int((count + 1)/2)
        self.result = sort[med_pos-1]

        return "{0:.2f}".format(round(self.result,2))

    def mode(self, data):
        count = []
        for k in range(len(data)):
            count.append(data.count(data[k]))
        max_pos = count.index(max(count))

        return data[max_pos]

    def variance1(self, data):
        meanx = self.mean(data)
        sumx = 0.0
        for k in range(len(data)):
            temp = self.calc.square(self.calc.subtract(data[k], meanx))
            sumx = self.calc.add(sumx, temp)

        return "{0:.2f}".format(round(sumx/(len(data)-1), 2))

    def variance2(self, data):
        meanx = self.mean(data)
        sumx = 0.0
        for k in range(len(data)):
            temp = self.calc.square(self.calc.subtract(data[k], meanx))
            sumx = self.calc.add(sumx, temp)

        return "{0:.2f}".format(round(sumx/(len(data)), 2))

    def standard_deviation(self, data):
        std = self.calc.square_root(self.variance1(data))

        return "{0:.2f}".format(round(std,2))

    def quartile(self, data):
        count = len(data)
        sort = sorted(data)
        q1_pos = int((count + 1)/4)
        q3_pos = int((count + 1)*3/4)
        q2_pos = q3_pos - q1_pos

        return [sort[q1_pos-1], sort[q2_pos-1], sort[q3_pos-1]]

    def skewness(self, data):
        skew = 3*(float(self.mean(data)) - float(self.median(data)))/float(self.standard_deviation(data))

    def sample_correlation(self, datax, datay):
        meanx = self.mean(datax)
        meany = self.mean(datay)
        sumprod = 0.0
        sumx = 0.0
        sumy = 0.0
        for k in range(len(datax)):
            temp = self.calc.multiply(self.calc.subtract(datax[k], meanx), self.calc.subtract(datay[k], meany))
            sumprod = self.calc.add(sumprod, temp)
            sumx = self.calc.add(sumx, self.calc.square(self.calc.subtract(datax[k], meanx)))
            sumy = self.calc.add(sumy, self.calc.square(self.calc.subtract(datay[k], meany)))
        corr = self.calc.division(sumprod, self.calc.multiply(self.calc.square_root(sumx), self.calc.square_root(sumy)))

        return "{0:.2f}".format(round(corr,2))

    def population_correlation(self, datax, datay):
        corrp = np.cov(datax, datay)[0][1]/(stat.stdev(datax)*stat.stdev(datay))

        return "{0:.2f}".format(round(corrp,2))

    def z_score(self, datax):
        meanx = self.mean(datax)
        stdx = self.calc.square_root(self.variance2(datax))
        zscore = []
        for k in range(len(datax)):
            diff = self.calc.subtract(datax[k], meanx)
            zscore.append(self.calc.division(diff, stdx))
        zscore = ["%.2f"%item for item in zscore]

        return [float(k) for k in zscore]

    def mean_deviation(self, datax):
        meanx = self.mean(datax)
        sumx = 0.0
        for k in range(len(datax)):
            diff = abs(self.calc.subtract(datax[k], meanx))
            sumx = self.calc.add(sumx, diff)
        mean_dev = self.calc.division(sumx, len(datax))

        return "{0:.2f}".format(round(mean_dev, 2))