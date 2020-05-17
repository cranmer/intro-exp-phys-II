#Yongning Lei (Intro to Experimental Phy Lab II) P = 2x

import numpy as np
from .base_distribution import BaseDistribution


class Dist_yl4874(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):

		return 2*x #normalizing lnx  in bounds 0,1 gives us the function

	def mean(self):

		return 0.609134  #integral of xf(x) = integral 2x**2 from 0 to 1

	def std(self):

		return np.sqrt(1/18) #sqrt variance = sqrt ( integral (x-2/3)^2 f(x))
