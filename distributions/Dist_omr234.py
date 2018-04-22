
import numpy as np
from .base_distribution import BaseDistribution

class Dist_omr234(BaseDistribution):
	def __init__(self):
		self.f_max = 2
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		y = 2*x
		return y

	def mean(self):
		"""This is the mean of the PDF"""
		return 1

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(1./6.)
