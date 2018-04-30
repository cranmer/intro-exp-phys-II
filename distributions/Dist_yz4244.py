
import numpy as np
from .base_distribution import BaseDistribution

class Dist_yz4244(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (x**4)

	def mean(self):
		"""This is the mean of the PDF"""
		return (1/6)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(13/140)
