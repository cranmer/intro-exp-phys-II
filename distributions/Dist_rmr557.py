import numpy as np
from .base_distribution import BaseDistribution

class Dist_rmr557(BaseDistribution):
	def __init__(self):
		self.f_max = 9.0/14
		self.x_min = 0
		self.x_max = 2


	def pdf(self, x):
		"""This is your PDF"""
		return (1.0/14)* (3.0*(x**2) - 6.0*x + 9.0)

	def mean(self):
		"""This is the mean of the PDF"""
		return 1

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(455) / 35 