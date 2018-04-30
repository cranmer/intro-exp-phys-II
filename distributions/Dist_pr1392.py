
import numpy as np
from .base_distribution import BaseDistribution

class Dist_pr1392(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return np.sin(x)**2

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt((1/6)((8*(np.pi**2)-3)))
