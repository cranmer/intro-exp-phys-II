import numpy as np
from base_distribution import BaseDistribution

'''Distribution of the z values of a short acrylic cylinder, measured in the 
Center for Soft Matter Research to determine flatness.'''

class Dist_jgc375(BaseDistribution):
	def __init__(self):
		self.f_max = 0.025
		self.x_min = 2099.45  
		self.x_max = 2161.475


	def pdf(self, x):
		"""This is your PDF"""
		mu, sigma = 2130.93795, 15.65586 # mean and standard deviation
                s = 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x - mu)**2 / (2 * sigma**2))
		return s

	def mean(self):
		"""This is the mean of the PDF"""
		return 2130.93795

	def std(self):
		"""This is the standard deviation of the pdf"""
		return 15.65586



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
		print("%s has errors. didn't work" %(cls.__name__))




















