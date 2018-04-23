
# coding: utf-8

# In[2]:


import numpy as np
from .base_distribution import BaseDistribution

class Dist_kd1726(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = pi/2
		self.x_max = 0


	def pdf(self, x):
		"""This is your PDF"""
		return sin(x)*(1).

	def mean(self):
		"""This is the mean of the PDF"""
		return -1

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 0

