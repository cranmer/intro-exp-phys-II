import numpy as np
from .base_distribution import BaseDistribution

class Dist_cmr653(BaseDistribution):
	def __init__(self):
		self.f_max = 27/76
		self.x_min = -2
		self.x_max = 2


	def pdf(self, x):
		"""This is your PDF"""
		return 3*(x**2 + 5)/76

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the PDF"""
		return np.sqrt(148/95)