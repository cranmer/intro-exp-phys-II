import numpy as np
from .base_distribution import BaseDistribution

class Dist_njg338(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = (np.pi)/2


	def pdf(self, x):
		return np.sqrt((np.cos(x))**2)

	def mean(self):
		return 0.571

	def std(self):
		return sqrt(0.142)