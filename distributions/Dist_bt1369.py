import numpy as np
from .base_distribution import BaseDistribution

class Dist_bt1369(BaseDistribution):
	def __init__(self):
		self.f_max = 0.22214
		self.x_min = 0.86288
		self.x_max = 8.44000


	def pdf(self, x):
		"""This is your PDF"""
		return np.abs(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 5.105308322606092.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.5)
