import numpy as np
from .base_distribution import BaseDistribution

class Dist_njg338(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -2*(np.pi)
		self.x_max = 2*(np.pi)


	def pdf(self, x):
		return ((np.cos(x))*(np.cos(x)))

	def mean(self):
		return 0

	def std(self):
		return np.sqrt(((8*(np.pi)*(np.pi)*(np.pi))+(3*(np.pi)))/3)
