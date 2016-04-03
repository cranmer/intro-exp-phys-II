
import numpy as np
from base_distribution import BaseDistribution

class Dist_msc565(BaseDistribution):
	def __init__(self):
		self.f_max = 2*np.log(2)
		self.x_min = 1
		self.x_max = 2


	def pdf(self, x):
		"""This is your PDF"""
		return np.log(x)*x

	def mean(self):
		"""This is the mean of the PDF"""
		return 1.0706147037154097140

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.271988)
