
import numpy as np
from .base_distribution import BaseDistribution

class Dist_fay221(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""PDF result = """
		return 1.

	def mean(self):
		"""PDF Mean = """
		return 0.5

	def std(self):
		"""PDF Standard Deviation = """
		return np.sqrt(1./12)
