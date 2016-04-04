import numpy as np
from base_distribution import BaseDistribution

class Dist_ry643(BaseDistribution):
    def __init__(self):
        self.f_max = 11
        self.x_min = -5
        self.x_max = 5


    def pdf(self, x):
        """This is your PDF"""
        return (x**3)+7

    def mean(self):
        """This is the mean of the PDF"""
        return 7

    def std(self):
        """This is the standard deviation of the pdf"""
        return np.sqrt(41030/11)
        
        