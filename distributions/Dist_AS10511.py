
import numpy as np
from .base_distribution import BaseDistribution

class As10511(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = (np.pi)/2


	def pdf(self, x):
		"""This is your PDF"""
		return np.cos(x)-np.sin(x)+(2)/(np.pi)

	def mean(self):
		"""This is the mean of the PDF"""
		return (3*np.pi)/4 - 2

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.02140)
