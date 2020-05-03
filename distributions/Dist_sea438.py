import numpy as np
from .base_distribution import BaseDistribution

class Dist_sea438(BaseDistribution):
	def __init__(self):
		self.f_max = 1.1
		self.x_min = 0
		self.x_max = 10


	def pdf(self, x):
		"""This is your PDF"""
		f_x = np.sin(x)+0.5
		Z = -np.cos(10) + 0.5(10) + np.cos(0)
		return f_x/Z
	

	def mean(self):
		"""This is the mean of the PDF"""
		Sum = 0
		for x in range(11):
			Sum += self.pdf(x)
		avg = Sum/11
		return avg

	def std(self):
		"""This is the standard deviation of the pdf"""
		Sum = 0
		mean = self.mean()
		for x in range(11):
			Sum += (x - mean)**2
		Sum /= 11
		return np.sqrt(Sum)

	