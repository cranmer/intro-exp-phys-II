import numpy as np
from .base_distribution import BaseDistribution

class Dist_speedreed(BaseDistribution):
	def __init__(self):
		self.f_max = 2
		self.x_min = -2
		self.x_max = 2


	def pdf(self, x):
		"""This is your PDF"""
		return np.abs(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 2*np.sqrt(0.5)
