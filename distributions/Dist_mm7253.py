
import numpy as np
from .base_distribution import BaseDistribution


    
    
class Dist_mm7253(BaseDistribution):
	def __init__(self):
		self.f_max = 1.245
		self.x_min = -1
		self.x_max = 1


	def pdf(self, x):
		"""This is your PDF"""
		return np.clip(((np.sqrt((2*x+4)**3)-5*(2*x)**4)/10)*(1/0.742897589721),a_min=0,a_max=None)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.119

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0.27


