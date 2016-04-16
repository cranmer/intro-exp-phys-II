import numpy as np
from base_distribution import BaseDistribution

class Dist_vmj226(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -2*np.pi
		self.x_max = 2*np.pi


	def pdf(self, x):
		"""This is your PDF"""
		return np.cos(x)

	def mean(self):
		"""This is the mean of the PDF"""
		return (self.x_max*np.sin(self.x_max)+np.cos(self.x_max))-(self.x_min*np.sin(self.x_min)+np.cos(self.x_min))

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt((((self.x_max**2)-2)*np.sin(self.x_max)+2*self.x_max*np.cos(self.x_max))-(((self.x_min**2)-2)*np.sin(self.x_min)+2*self.x_min*np.cos(self.x_min)))

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


			print("%s passes tests, adding it" %(cls.__name__))
	except:
		print("%s has errors't work" %(cls.__name__))

if __name__ == '__main__':
	test(Dist_vmj226)