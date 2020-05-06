import numpy as np
from .base_distribution import BaseDistribution

class Dist_tt1392(BaseDistribution):
	def __init__(self):
		self.f_max = 0.32
		self.x_min = -pi
		self.x_max = pi 


	def pdf(self, x):
		"""This is your PDF"""
		return 1/np.pi * np.cos**{2}x

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 1.9.