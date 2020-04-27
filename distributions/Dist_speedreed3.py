import numpy as np
 from .base_distribution import BaseDistribution

 class Dist_speedreed3(BaseDistribution):
 	def __init__(self):
 		self.f_max = 3
 		self.x_min = -3
 		self.x_max = 1


 	def pdf(self, x):
 		"""This is your PDF"""
 		return np.abs(x)

 	def mean(self):
 		"""This is the mean of the PDF"""
 		return 0.

 	def std(self):
 		"""This is the standard deviation of the pdf"""
 		return 3*np.sqrt(0.5)
