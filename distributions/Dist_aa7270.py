import numpy as np
from .base_distribution import BaseDistribution

class Dist_aa7270(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 4

    def f(x):
        return x^3/4

	def pdf(self, x):
		"""This is your PDF"""
		return x^3/64

	def mean(self):
		"""This is the mean of the PDF"""
		return 3.2

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.43)


