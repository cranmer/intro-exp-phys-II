
import numpy as np
from .base_distribution import BaseDistribution

class Dist_os852(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -1
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt(abs(x))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.00452653628432

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.6545248448388085
