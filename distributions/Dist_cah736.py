import numpy as np
from .base_distribution import BaseDistribution

class Dist_cah736(BaseDistribution):
	def __init__(self):
		self.f_max = 1.166
		self.x_min = 0
		self.x_max = 6


	def pdf(self, x):
		"""This is your PDF"""
		return ((np.sin(x)**2))/(1.55595*x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 2.0143

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(2.25669)
