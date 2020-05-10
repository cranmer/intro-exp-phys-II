import numpy as np
from .base_distribution import BaseDistribution

class Dist_jdg577(BaseDistribution):
	def __init__(self):
		self.f_max = 2/(np.e * np.sqrt(2*np.pi))
		self.x_min = -10
		self.x_max = 10


	def pdf(self, x):
		return (x ** 2) * (np.exp(-x ** 2 / 2))/np.sqrt(2*np.pi)


	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(3)