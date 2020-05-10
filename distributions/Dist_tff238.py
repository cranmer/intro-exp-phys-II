import numpy as np
from .base_distribution import BaseDistribution

class Dist_tff238(BaseDistribution):
	def __init__(self):
		self.f_max = .96426
		self.x_min = -1
		self.x_max = 3


	def pdf(self, x):
		"""This is your PDF"""
		return (.10714)*x*x

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.249993

	def std(self):
		"""This is the standard deviation of the pdf"""
		return .35211
