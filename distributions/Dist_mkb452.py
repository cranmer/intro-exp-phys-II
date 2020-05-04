import numpy as np
from .base_distribution import BaseDistribution

class Dist_mkb452(BaseDistribution):
	def __init__(self):
		self.f_max = 0.5
		self.x_min = 2
		self.x_max = 5


	def pdf(self, x):
		"""This is your PDF"""
		y = (1/0.000022737)
		return (y*np.exp(-x,3)*np.sin(x))

	def mean(self):
		"""This is the mean of the PDF"""
		return 2.06994

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.066015


