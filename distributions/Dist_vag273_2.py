
import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution

class Dist_vag273_2(BaseDistribution):
	def __init__(self):
		self.f_max = 2/np.sqrt(pi)
		self.x_min = 0
		self.x_max = 2/np.sqrt(pi)
=======
from .base_distribution import BaseDistribution

class Dist_vag273_2(BaseDistribution):
	def __init__(self):
		self.f_max = 2/np.sqrt(np.pi)
		self.x_min = 0
		self.x_max = 2/np.sqrt(np.pi)
>>>>>>> cranmer/master


	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt((4/np.pi)-(x**2))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.48

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.09)
