#Aditya Pandey (Intro Experimental II) P = x^3
#Date Submitted 4/22/2018

import numpy as np
from .base_distribution import BaseDistribution


class Dist_ap5312(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		
		return (4*np.power(x,3)) #normalizing x^3  in bounds 0,1 gives us the function 4x^3

	def mean(self):
		
		return (0.8)  #integral of xf(x) = integral 4x^5 = 4/5 x^5 from 0 to 1

	def std(self):
		
		return np.sqrt(.026667) #sqrt variance = sqrt ( integral (x-.8)^2 f(x))
