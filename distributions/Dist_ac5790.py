import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution
=======
from .base_distribution import BaseDistribution
>>>>>>> cranmer/master

class Dist_ac5790(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -10001
		self.x_max = -10000


	def pdf(self, x):
		"""This is your PDF"""
<<<<<<< HEAD
		return 1
=======
		return 1.
>>>>>>> cranmer/master

	def mean(self):
		"""This is the mean of the PDF"""
		return -10000.5

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(1./12)
