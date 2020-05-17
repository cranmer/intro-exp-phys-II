import numpy as np
import math
from .base_distribution import BaseDistribution

class Dist_njg338(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -2*(math.pi)
		self.x_max = 2*(math.pi)


	def pdf(self, x):
		return ((math.cos(x))**2)

	def mean(self):
		return 0

	def std(self):
		return math.sqrt(((8*((math.pi)**3))+(3*(math.pi)))/3)