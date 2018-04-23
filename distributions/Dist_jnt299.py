
import numpy as np
from .base_distribution import BaseDistribution

class Dist_jnt299(BaseDistribution):
	def __init__(self):
		self.f_max = 8
		self.x_min = 0
		self.x_max = 0.14088


	def pdf(self, x):
		"""This is your PDF"""
		return x**3 + 2x**2 - 13x + 8

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.067480

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.00164585
