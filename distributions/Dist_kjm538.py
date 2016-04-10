import numpy as np
from base_distribution import BaseDistribution

class Dist_kjm538(BaseDistribution):
	def __init__(self):
		self.f_max = 1.6094
		self.x_min = 1.
		self.x_max = 6.


	def pdf(self, x):
		"""This is your PDF"""
		return (4./23.)*np.log(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return (1./23.)*((self.x_max**2 * np.log(self.x_max**2))
		-(self.x_max**2)+1)

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt((4./23.)*((-((self.x_max**3)/9.)+
		(50110707.*(np.log(self.x_max)-1))/500000.)
		+(((self.x_max**3)/3.)*np.log(self.x_max))-(36783./500.)*
		(np.log(self.x_max**2)-1))+(5780027./2250000.))
