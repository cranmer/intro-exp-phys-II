import numpy as np
from .base_distribution import BaseDistribution


class Dist_ejt352(BaseDistribution):
	def __init__(self):
		self.f_max = (12/24)
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return (11/24)*((x**5)+(7/8)*x**2)
     #   """This function from 0 to 1 = (11/24)"""

	def mean(self):
		"""This is the mean of the PDF"""
		return 243/308

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt((35841/1043504))


        