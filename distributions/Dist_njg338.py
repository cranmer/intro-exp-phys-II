import numpy as np
from .base_distribution import BaseDistribution

class Dist_njg338(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -2
		self.x_max = 2


	def pdf(self, x):
		return np.pi

	def mean(self):
		return np.pi

	def std(self):
		return np.sqrt(((12*((np.pi)**3))+(16*(np.pi)))/3)