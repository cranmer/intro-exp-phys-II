import numpy as np
from .base_distribution import BaseDistribution

class Dist_npl248(BaseDistribution):
	def __init__(self):
		self.f_max = (5*(np.pi**2))/4
		self.x_min = 1
		self.x_max = -1


	def pdf(self, x):
		"""This is your PDF"""
		return (2/((3*(np.pi**2))-16))*((np.arcsin(x))**2)+((np.arccos(x))**2)

	def mean(self):
		"""This is the mean of the PDF"""
		return -((np.pi**2)/4)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return sqrt(((np.pi**2)/2)-(56/27))
