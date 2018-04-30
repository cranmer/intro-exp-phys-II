import numpy as np
from .base_distribution import BaseDistribution

class Dist_(BaseDistribution):
	def __init__(self):
		self.f_max = 5
		self.x_min = 0
		self.x_max = .5


	def pdf(self, x):
		"""This is your PDF"""
		return 10*x

	def mean(self):
		"""This is the mean of the PDF"""
		return 2.5

	def std(self):
		"""This is the standard deviation of the pdf"""
		return .8537
