import numpy as np
from .base_distribution import BaseDistribution

class Dist_cas955(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (-1.5*x**4+7*x**2)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 8*np.sqrt(19./35)
