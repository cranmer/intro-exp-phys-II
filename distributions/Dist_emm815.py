import numpy as np
from .base_distribution import BaseDistribution

class Dist_emm815(BaseDistribution):
	def __init__(self):
		self.f_max = 3
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return 3*x**2

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.75

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.0375)