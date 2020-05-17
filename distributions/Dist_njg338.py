import numpy as np
from .base_distribution import BaseDistribution

class Dist_njg338(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -6.28
		self.x_max = 6.28


	def pdf(self, x):
		return ((np.cos(x))**2)

	def mean(self):
		return 0

	def std(self):
		return np.sqrt(((8*(np.pi)*(np.pi)*(np.pi))+(3*(np.pi)))/3)