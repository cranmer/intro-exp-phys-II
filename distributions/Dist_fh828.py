
import numpy as np
from .base_distribution import BaseDistribution

class Dist_fh828(BaseDistribution):
	def __init__(self):
		self.f_max = np.pi/2
		self.x_min = -.5
		self.x_max = .5


	def pdf(self, x):
		"""This is your PDF"""
		return (np.pi*0.5*np.cos(np.pi*x))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0

	def std(self):
		"""This is the standard deviation of the pdf"""
		return ((np.pi-2)/(2*np.pi))
