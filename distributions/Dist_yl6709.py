import numpy as np
from .base_distribution import BaseDistribution

class Dist_at4227(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -1
		self.x_max = 4


	def pdf(self, x):
		return np.abs(x)

	def mean(self):
		return 1.5

	def std(self):
		return np.sqrt(0.5)
