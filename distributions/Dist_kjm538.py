import numpy as np
from base_distribution import BaseDistribution

class Dist_kjm538(BaseDistribution):
	def __init__(self):
		self.f_max = 1.61
		self.x_min = 1
		self.x_max = 5


	def pdf(self, x):
		"""This is your PDF"""
		return np.log(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 3.49

	def std(self):
		"""This is the standard deviation of the pdf"""
		return .998


