import numpy as np
from .base_distribution import BaseDistribution

class Dist_zs1427(BaseDistribution):
	def __init__(self):
		self.f_max = 4
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return 4*x**3
	
	def mean(self):
		"""This is the mean of the PDF"""
		return 0.8 

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 2/75

