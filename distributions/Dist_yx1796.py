import numpy as np
from .base_distribution import BaseDistribution

class Dist_yx1796(BaseDistribution):
	def __init__(self):
		self.f_max = 64/60
		self.x_min = 2
		self.x_max = 4


	def pdf(self, x):
		"""This is your PDF"""
		return (x**3)/60

	def mean(self):
		"""This is the mean of the PDF"""
		return 3.3

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.266)


