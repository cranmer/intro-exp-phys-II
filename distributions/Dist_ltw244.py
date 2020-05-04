import numpy as np
from .base_distribution import BaseDistribution


class Dist_ltw244(BaseDistribution):

    def __init__(self):
        self.f_max = 1.5
        self.x_min = 0
        self.x_max = 2

    def pdf(self, x):
        """This is your PDF"""
        return (x**3 - x**2 + 1) / (10/3)

    def mean(self):
        """This is the mean of the PDF"""
        return 1.32

    def std(self):
        """This is the standard deviation of the pdf"""
        return 0.581033561853


