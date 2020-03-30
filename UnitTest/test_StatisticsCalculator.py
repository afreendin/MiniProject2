import sys
import random
import numpy as np
from numpy.random import randn
sys.path.append('../DescriptiveStatisticsFunction')
sys.path.append('../HelperFunctions')
from HelperFunctions.HelperFunctions import lib_mean
from HelperFunctions.HelperFunctions import lib_median
from HelperFunctions.HelperFunctions import lib_mode
from HelperFunctions.HelperFunctions import lib_variance
from HelperFunctions.HelperFunctions import lib_standard_deviation
from HelperFunctions.HelperFunctions import lib_skewness
from HelperFunctions.HelperFunctions import lib_sample_correlation
from HelperFunctions.HelperFunctions import lib_zscore

from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_mean
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_median
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_mode
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_variance1
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_variance2
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_standard_deviation
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_quartile
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_skewness
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_sample_correlation
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_population_correlation
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_zscore
from DescriptiveStatisticsFunction.DescriptiveStatisticsFunction import created_mean_deviation

from DescriptiveStatisticsFunction import DescriptiveStatisticsFunction
from HelperFunctions import HelperFunctions
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.val_int = random.sample(range(1,100), 13)
        # self.libStat = HelperFunctions
        # self.createStat = DescriptiveStatisticsFunction

        self.mode_data = random.choices(range(10), k= 10)
        self.quartile_data = [10, 20, 30, 40, 50, 60, 70]

        self.datax = np.array(20*randn(10) + 100).tolist()
        self.datay = self.datax + (10*randn(10) + 50)

    def test_mean_calculator(self):
        self.assertEqual(created_mean(self.val_int), lib_mean(self.val_int))

    def test_median_calculator(self):
        self.assertEqual(created_median(self.val_int), lib_median(self.val_int))

    def test_mode_calculator(self):
        self.assertEqual(created_mode(self.val_int), lib_mode(self.val_int))

    def test_variance_calculator(self):
        self.assertEqual(created_variance1(self.val_int), lib_variance(self.val_int))

    def test_stdev_calculator(self):
        self.assertEqual(created_standard_deviation(self.val_int), lib_standard_deviation(self.val_int))

    def test_quartile_calculator(self):
        self.assertEqual(created_quartile(self.quartile_data), [20, 40, 60])

    def test_skewness_calculator(self):
        self.assertEqual(created_skewness(self.val_int), lib_skewness(self.val_int))

    def test_correlation_calculator(self):
        created_correlation = created_sample_correlation(self.datax, self.datay)
        lib_correlation = lib_sample_correlation(self.datax, self.datay)
        self.assertEqual(created_correlation, "{0:.2f}".format(round(lib_correlation[0],2)))

    def test_zscore(self):
        self.assertEqual(created_zscore(self.datax), lib_zscore(self.datax))



if __name__ == '__main__':
    unittest.main()
