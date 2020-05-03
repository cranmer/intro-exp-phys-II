import math as math
import numpy as np
from .base_distribution import BaseDistribution

class Dist_sj2879(BaseDistribution):
	def __init__(self):
		self.f_max = 36
		self.x_min = -3
		self.x_max = 3

	def pdf(self, x):
		"""This is your PDF"""
		return (x**2)/(18) #4x^2 normalized over range of [-3, 3] gives this pdf

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt((27)/5)