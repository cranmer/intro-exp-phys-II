
import numpy as np
from .base_distribution import BaseDistribution

class Dist_kc90_3(BaseDistribution):
	def __init__(self):
		self.f_max = 1./3 / np.pi
		self.x_min = -3*np.pi
		self.x_max = 3*np.pi


	def pdf(self, x):
		"""This is your PDF"""
		return np.sin(x)**2 / 3 / np.pi

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(3.*np.pi**2 - 0.5)
