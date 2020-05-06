import numpy as np
from .base_distribution import BaseDistribution

class Dist_sk7372(BaseDistribution):
	def __init__(self):
		self.f_max = 1.5 #maximum value of pdf at x=1
		self.x_min = -1
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return 1.5 * np.power(x,2) ##obtained after finding z from integrating x^2 from -1 to 1

	def mean(self):
		"""This is the mean of the PDF"""
		return 0. #obtained by integrating 1.5x^3 from -1 to 1

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.6) #obtained by integrating 1.5x^4 from -1 to 1