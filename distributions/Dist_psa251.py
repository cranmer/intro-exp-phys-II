# -*- coding: utf-8 -*-

import numpy as np

import traceback

from base_distribution import BaseDistribution

class Dist_psa251(BaseDistribution):
    # Ditched exp. distribution
    # theory never matched RVS
    # despite the number of calculations and recalculations
    #
    # instead: p(x) = 1 - x^2

    def __init__(self):
        self.x_min = -1.
        self.x_max = 1.
        self.f_max = 1.

    def pdf(self, x):
        return 1. - x**2.

    def mean(self):
        return 0.

    def std(self):
        return np.sqrt(4./15.)

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
        print traceback.print_exc()

if __name__ == '__main__':
	test(Dist_psa251)
