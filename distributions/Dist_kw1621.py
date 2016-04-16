import numpy as np
from base_distribution import BaseDistribution

class Dist_kw1621(BaseDistribution):
	def __init__(self):
		self.f_max = 100./77.
		self.x_min = -10
		self.x_max = 10


        def Normalization(self, x):
            temp = (32 * x**3 - 12 *x * np.cos(4 *x) + (3 - 24 *x**2) * np.sin(4 *x) )/768
            #print(temp)
            return temp 
            
	def pdf(self, x):
		"""This is your PDF"""
		return ((np.sin(x)*np.cos(x)*x))**2 / (self.Normalization(self.x_max) - self.Normalization(self.x_min))

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		"""(128 x^5 - 20 x (-3 + 8 x^2) Cos[4 x] - 5 (3 - 24 x^2 + 32 x^4) Sin[4 x])/5120"""
		return np.sqrt(4579.3)/np.sqrt((self.Normalization(self.x_max) - self.Normalization(self.x_min)))
		
		
def test(cls):
	try:
		dist = cls()
		N_test = 10000
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
	test(Dist_kw1621)
