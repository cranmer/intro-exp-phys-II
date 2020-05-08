import numpy as np
from .base_distribution import BaseDistribution

class Dist_aew492(BaseDistribution):
	def __init__(self):
		self.f_max = 0.85
		self.x_min = 0
		self.x_max = 1.5


	def pdf(self, x):
		"""This is your PDF"""
		return (1/1.677)*(np.sin(x**2)+np.cos(x**2))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.7174

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.3878


