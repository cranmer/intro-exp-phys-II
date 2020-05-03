import numpy as np
from .base_distribution import BaseDistribution

class Dist_ajt540(BaseDistribution):
	def __init__(self):
		self.f_max = 2.19566
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (420/307.0)*(5*x**6 - 17*x**5 + 3*x**4 + 9*x**3)

	def mean(self):
		"""This is the mean of the PDF"""
		return (417.0/614.0)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(34003.0/1130988.0)
		