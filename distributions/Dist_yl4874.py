#Yongning Lei (Intro to Experimental Phy Lab II) P = x^4

import numpy as np
from .base_distribution import BaseDistribution


class Dist_yl4874(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):

		return 5*x**4 #normalizing lnx  in bounds 0,1 gives us the function

	def mean(self):

		return (5/6)  #integral of xf(x) = integral x*abs(lnx) from 0 to 1

	def std(self):

		return np.sqrt(5/252) #sqrt variance = sqrt ( integral (x-0.25)^2 f(x))
