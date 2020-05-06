import numpy as np
from .base_distribution import BaseDistribution

class Dist_kas938(BaseDistribution):
	def __init__(self):
		self.f_max = 1.019
		self.x_min = 0
		self.x_max = 3


	def pdf(self, x):
		"""This is your PDF"""
		return ( math.exp(-x**2) + math.exp(-2*(x-2)**2) )

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.703656

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 1.70755
