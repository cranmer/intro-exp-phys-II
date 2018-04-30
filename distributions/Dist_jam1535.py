import math
import numpy as np
from .base_distribution import BaseDistribution

class Dist_kc90(BaseDistribution):
	def __init__(self):
		self.f_max = 5.6133*math.exp(-1)
		self.x_min = -1
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return math.exp(-1/(x*x))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return .842623
