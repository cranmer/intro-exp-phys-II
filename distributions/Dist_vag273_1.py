
import numpy as np
from base_distribution import BaseDistribution

class Dist_vag273_1(BaseDistribution):
	def __init__(self):
		self.f_max = 2
		self.x_min = 0
		self.x_max = 0.5


	def pdf(self, x):
		"""This is your PDF"""
		return 2.

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.25

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(1./12)
