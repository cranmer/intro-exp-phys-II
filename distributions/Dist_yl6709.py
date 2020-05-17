import numpy as np
from .base_distribution import BaseDistribution

class Dist_yl6709(BaseDistribution):
	def __init__(self):
		self.f_max = 1.55088319692
		self.x_min = -np.pi/2
		self.x_max = np.pi/2

	def pdf(self, x):
		return np.cos(x)*np.exp(x)/(np.exp(np.pi/2)+np.exp(-np.pi/2))*2

	def mean(self):
		return 0.440659519978

	def std(self):
		return 0.626020165626
