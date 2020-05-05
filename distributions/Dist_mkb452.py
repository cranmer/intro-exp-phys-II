import numpy as np
from .base_distribution import BaseDistribution

class Dist_mkb452(BaseDistribution):
	def __init__(self):
		self.f_max = 13.5
		self.x_min = 2
		self.x_max = 2.4


	def pdf(self, x):
		"""This is your PDF"""
		y = (1/0.000022737)
		return (y*np.exp((np.power(-x,3)))*np.sin(x))

	def mean(self):
		"""This is the mean of the PDF"""
		return 2.06619

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.06436


