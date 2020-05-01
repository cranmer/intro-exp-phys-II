import numpy as np
from .base_distribution import BaseDistribution

class Dist_zs1427(BaseDistribution):
	def __init__(self):
		self.f_max = 50
		self.x_min = 0.02
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (1/x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.98 

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 2.3361

