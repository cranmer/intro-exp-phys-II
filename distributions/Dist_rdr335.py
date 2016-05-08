import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution
=======
from .base_distribution import BaseDistribution
>>>>>>> cranmer/master

class Dist_rdr335(BaseDistribution):
	def __init__(self):
		self.f_max = np.sqrt(2/np.pi)
		self.x_min = -np.sqrt(2/np.pi)
		self.x_max = np.sqrt(2/np.pi)
		
	def pdf(self, x):
		"""This is your PDF"""
		return np.sqrt(2/np.pi - x**2)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.1
