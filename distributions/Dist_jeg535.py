
import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution
=======
from .base_distribution import BaseDistribution
>>>>>>> cranmer/master

class Dist_jeg535(BaseDistribution):
	def __init__(self):
		self.f_max = 72
		self.x_min = -7.2
		self.x_max = .72


	def pdf(self, x):
		"""This is your PDF"""
<<<<<<< HEAD
		return np.abs(x+7.2)
=======
		return np.cos(x)
>>>>>>> cranmer/master

	def mean(self):
		"""This is the mean of the PDF"""
		return .072

	def std(self):
		"""This is the standard deviation of the pdf"""
<<<<<<< HEAD
		return np.sqrt(0.27)
=======
		return np.sqrt(0.27)
>>>>>>> cranmer/master
