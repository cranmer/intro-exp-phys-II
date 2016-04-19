# -*- coding: utf-8 -*-

import numpy as np

import traceback

from base_distribution import BaseDistribution

class Dist_psa251_2(BaseDistribution):
    # Trying exp. dist again
    # this time with improper bounds (D: [0, ∞))
    #
    # p(x) = λe^(-λx)

    def __init__(self):
        self.lamda = 1.

        self.x_min = 0.
        self.x_max = 10 # good enough for an inf approximation?
        self.f_max = self.lamda

        # self._k = 1

    def pdf(self, x):
        # print self._k
        #
        # self._k += 1
        return self.lamda*np.exp((-1.)*self.lamda*x)

    def mean(self):
        return (1./self.lamda)

    def std(self):
        mu_sq = (1./self.lamda)**2.

        return np.sqrt(mu_sq) # might as well return mu, but this form is from Integral[(x - µ)^2 * p(x) * dx]


def test(cls):
	try:
		dist = cls()
		N_test = 100000
		rvs = dist.rvs(N_test)
		if np.abs(np.mean(rvs) - dist.mean()) > 2*np.std(rvs)/np.sqrt(N_test):
			print("means don't match for %s: %f vs. %f" %(cls.__name__,
														  np.mean(rvs), dist.mean()))

		elif np.abs(np.std(rvs) - dist.std()) > 2*np.std(rvs)/np.sqrt(np.sqrt(1.*N_test)):
			print("std devs. don't match for %s: %f vs. %f" %(cls.__name__,
														  np.std(rvs), dist.std()))

		elif np.sum(dist.pdf(np.linspace(dist.x_min,dist.x_max,100))<0) > 0:
			print("pdf was negative in some places")

		else:
			print("%s passes tests, adding it" %(cls.__name__))
	except:
		print("%s has errors. didn't work" %(cls.__name__))
        print traceback.print_exc()

if __name__ == '__main__':
	test(Dist_psa251_2)
