import numpy as np
from .base_distribution import BaseDistribution

class Dist_speedreed4(BaseDistribution):
	def __init__(self):
		self.f_max = 4
		self.x_min = -4
		self.x_max = 4


	def pdf(self, x):
		"""This is your PDF"""
		return np.abs(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 4*np.sqrt(0.5)
