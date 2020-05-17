import numpy as np
from .base_distribution import BaseDistribution

class Dist_sdl433(BaseDistribution):
	def __init__(self):
		self.x_min = 0
		self.x_max = 1
		self.f_max = 3

   	##U-quad distribution for domain [0, 1]
	def pdf(self, x):
		return 12 * ((x - 0.5) ** 2)
	
	#Returns mean of the pdf
	def mean(self):
        	return 0.5
	
	#Returns standard deviation of the pdf
	def std(self):
		return np.sqrt(0.15)
