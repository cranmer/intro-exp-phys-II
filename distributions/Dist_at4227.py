import numpy as np
from .base_distribution import BaseDistribution
class Dist_at4227(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = np.pi


	def pdf(self, x):
		return np.sin(x)/2

	def mean(self):
		return np.pi/2

	def std(self):
		return .683667