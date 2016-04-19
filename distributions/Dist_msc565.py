
import numpy as np
from base_distribution import BaseDistribution

class Dist_msc565(BaseDistribution):
	def __init__(self):
		self.f_max = 2
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (((x-0.5)**3)+0.125)*8

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.6

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.07333333333333333333333)
