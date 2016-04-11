import numpy as np
from base_distribution import BaseDistribution

'''Distribution of the z values of a short acrylic cylinder, measured in the 
Center for Soft Matter Research to determine flatness.'''

class Dist_jgc375(BaseDistribution):
	def __init__(self):
		self.f_max = 2161.475
		self.x_min = 1
		self.x_max = 1000


	def pdf(self, x):
		"""This is your PDF"""
		mu, sigma = 2130.93795, 15.65586 # mean and standard deviation
                s = 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x - mu)**2 / (2 * sigma**2))
		return s

	def mean(self):
		"""This is the mean of the PDF"""
		return 2130.93795

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 15.65586
























