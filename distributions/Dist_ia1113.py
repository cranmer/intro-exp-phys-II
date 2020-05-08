import numpy as np
from .base_distribution import BaseDistribution

class Dist_ia1113(BaseDistribution):
	def __init__(self):
		self.f_max = 2.541
		self.x_min = 7.0
		self.x_max = 7.5


	def pdf(self, x):
		"""This is your PDF"""
		return np.exp(x)/711.409

	def mean(self):
		"""This is the mean of the PDF"""
		return 7.271

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.020576)