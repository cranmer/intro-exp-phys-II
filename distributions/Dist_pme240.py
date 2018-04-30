
import numpy as np
from .base_distribution import BaseDistribution

class Dist_pme240(BaseDistribution):
	def __init__(self):
		self.f_max = 3
		self.x_min = 0
		self.x_max = .32936


	def pdf(self, x):
		"""This is your PDF"""
		return x**2 + 3

	def mean(self):
		"""This is the mean of the PDF"""
		return .1656589

	def std(self):
		"""This is the standard deviation of the pdf"""
		return .040377
