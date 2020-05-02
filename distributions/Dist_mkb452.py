import numpy as np
from .base_distribution import BaseDistribution

class Dist_mkb452(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -np.inf
		self.x_max = np.inf


	def pdf(self, x):
		"""This is your PDF"""
		y = (-np.square(x))/2
		return ((1/(np.sqrt(2*np.pi)))np.exp(y))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 1


