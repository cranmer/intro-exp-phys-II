import numpy as np
from .base_distribution import BaseDistribution

class Dist_kc90(BaseDistribution):
	def __init__(self):
		self.f_max = 0.9340322474
		self.x_min = -(1+5**(1/2))/2 
		self.x_max = 1/137


	def pdf(self, x):
		"""This is your PDF"""
		return 1.1064101553*np.sin(2**(x))

    def mean(self):
		"""This is the mean of the PDF"""
		return -0.6757350573

	
	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.455796824


