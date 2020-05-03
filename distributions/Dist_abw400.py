import numpy as np
from .base_distribution import BaseDistribution

class Dist_abw400(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt(x)/(2/3)

	def mean(self):
		"""This is the mean of the PDF"""
		return (2/5)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return (19/150)