import numpy as np
from .base_distribution import BaseDistribution

class Dist_mga357(BaseDistribution):
	def __init__(self):
		self.f_max = np.e
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return np.exp(x)/(np.e-1)

	def mean(self):
		"""This is the mean of the PDF"""
		return 1/(np.e-1)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.079326
