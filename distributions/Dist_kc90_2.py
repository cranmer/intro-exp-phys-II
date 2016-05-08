
import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution
=======
from .base_distribution import BaseDistribution
>>>>>>> cranmer/master

class Dist_kc90_2(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return 1.

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.5

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(1./12)
