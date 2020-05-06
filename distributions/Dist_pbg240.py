
import numpy as np
from .base_distribution import BaseDistribution

class Dist_pbg240(BaseDistribution):
	def __init__(self):
		self.f_max = 2*(3/16)
		self.x_min = 0
		self.x_max = 4


	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt(x)*(3/16)


	def mean(self):
		"""This is the mean of the PDF"""
		return 3.2

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 9.2647
