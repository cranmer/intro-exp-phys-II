# -*- coding: utf-8 -*-

import numpy as np
from .base_distribution import BaseDistribution

class Dist_knd286(BaseDistribution):
	def __init__(self):
		self.f_max = 1.76
		self.x_min = 0
		self.x_max = np.pi/2


	def pdf(self, x):
		"""This is your PDF"""
		return x*x*np.cos(x)*(4/(np.pi*np.pi-8))

	def mean(self):
		"""This is the mean of the PDF"""
		return (48-24*np.pi+np.pi**3)/(2*(np.pi**2-8))

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.09428259456016345559338193)
		
## Note: the unapproximated standard deviation is: the square root of 
## the integral integral from 0 to pi/2 of 
## x^2cos(x)*4/(pi^2-8)[x-(48-24 π + π^3)/(2 (-8 + π^2))]^2
## so I just plugged this into wolfram alpha and copy and pasted 
## the decimal approximation. I doulbe checked the approximated
## value with my accept reject program and i get the same thing.