import numpy as np
from base_distribution import BaseDistribution

class Dist_ak5606(BaseDistribution):
	def __init__(self):
		self.f_max = 8
		self.x_min = -2
		self.x_max = 2

	def pdf(self, x):
		"""This is your PDF"""
		return (x**2)+4

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(((((self.x_max**5.)/5.)+((self.x_max**3.)*4/3.)) - (((self.x_min**5.)/5.)+((self.x_min**3.)*4/3.))))


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
	test(Dist_ak5606)