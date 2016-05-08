
import numpy as np
<<<<<<< HEAD
from base_distribution import BaseDistribution

class Dist_ptf223(BaseDistribution):
	def __init__(self):
		self.f_max = 14
		self.x_min = -1
		self.x_max = 1
=======
from .base_distribution import BaseDistribution

class Dist_ptf223(BaseDistribution):
	def __init__(self):
		self.f_max = 10
		self.x_min = 0
		self.x_max = 10
>>>>>>> cranmer/master


	def pdf(self, x):
		"""This is your PDF"""
<<<<<<< HEAD
		return np.abs(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.5)
=======
		return 5*np.sin(x/2*np.pi)**2

	def mean(self):
		"""This is the mean of the PDF"""
		return (self.x_max+self.x_min)/2

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(4.6225)
>>>>>>> cranmer/master


def test(cls):
	try:
		dist = cls()
		N_test = 100000
		rvs = dist.rvs(N_test)
		if np.abs(np.mean(rvs) - dist.mean()) > 5*np.std(rvs)/np.sqrt(N_test):
			print("means don't match for %s: %f vs. %f" %(cls.__name__, 
														  np.mean(rvs), dist.mean()))
			
		elif np.abs(np.std(rvs) - dist.std()) > 5*np.std(rvs)/np.sqrt(np.sqrt(1.*N_test)):
			print("std devs. don't match for %s: %f vs. %f" %(cls.__name__, 
														  np.std(rvs), dist.std()))
		
		elif np.sum(dist.pdf(np.linspace(dist.x_min,dist.x_max,100))<0) > 0:
			print("pdf was negative in some places")

		else:
			print("%s passes tests, adding it" %(cls.__name__))
	except:
		print("%s has errors't work" %(cls.__name__))

if __name__ == '__main__':
<<<<<<< HEAD
	test(Dist_ptf223)
=======
	test(Dist_ptf223)
>>>>>>> cranmer/master
