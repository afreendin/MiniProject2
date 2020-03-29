import sys
import random
import numpy as np
from numpy.random import randn
sys.path.append('../DescriptiveStatisticsFunction')
sys.path.append('../HelperFunctions')
from DescriptiveStatisticsFunction import DescriptiveStatisticsFunction
from HelperFunctions import HelperFunctions
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:

        self.val_int = random.sample(range(1,100), 10)
        self.createStat = DescriptiveStatisticsFunction()
        self.libStat = HelperFunctions()

        self.mode_data = random.choices(range(10), k= 10)
        self.quartile_data = [10, 20, 30, 40, 50, 60, 70]

        self.datax = np.array(20*randn(10) + 100).tolist()
        self.datay = self.datax + (10*randn(10) + 50)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.createStat, DescriptiveStatisticsFunction)

    def test_mean_calculator(self):
        created_mean = self.createStat.mean(self.val_int)
        lib_mean = self.libStat.mean(self.val_int)
        self.assertEqual(created_mean, lib_mean)

    def test_median_calculator(self):
        created_median = self.createStat.median(self.val_int)
        lib_median = self.libStat.median(self.val_int)
        self.assertEqual(created_median, lib_median)

    def test_mode_calculator(self):
        created_mode = self.createStat.mode(self.mode_data)
        lib_mode = self.libStat.mode(self.mode_data)
        self.assertEqual(created_mode, lib_mode)

    def test_variance_calculator(self):
        created_variance = self.createStat.variance1(self.val_int)
        lib_variance = self.libStat.variance(self.val_int)
        self.assertEqual(created_variance, lib_variance)

    def test_stdev_calculator(self):
        created_stdev = self.createStat.standard_deviation(self.val_int)
        lib_stdev = self.libStat.standard_deviation(self.val_int)
        self.assertEqual(created_stdev, lib_stdev)

    def test_quartile_calculator(self):
        created_quartile = self.createStat.quartile(self.quartile_data)
        # lib_quartile = self.libStat.quartile(self.quartile_data)
        self.assertEqual(created_quartile, [20, 40, 60])

    def test_skewness_calculator(self):
        created_skewness = self.createStat.skewness(self.val_int)
        lib_skewness = self.libStat.skewness(self.val_int)
        self.assertEqual(created_skewness, lib_skewness)

    def test_correlation_calculator(self):
        created_correlation = self.createStat.sample_correlation(self.datax, self.datay)
        lib_correlation = self.libStat.sample_correlation(self.datax, self.datay)
        self.assertEqual(created_correlation, "{0:.2f}".format(round(lib_correlation[0],2)))

    def test_zscore(self):
        created_zscore = self.createStat.z_score(self.datax)
        lib_zscore = self.libStat.z_score(self.datax)
        self.assertEqual(created_zscore, lib_zscore)

if __name__ == '__main__':
    unittest.main()
