import numpy as np
from .base_distribution import BaseDistribution

class Dist_tt1392(BaseDistribution):
	def __init__(self):
		self.f_max = 0.56
		self.x_min = -inf
		self.x_max = inf


	def pdf(self, x):
		"""This is your PDF"""
		return 1/np.sqrt(pi) e^(-x^2)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.5)