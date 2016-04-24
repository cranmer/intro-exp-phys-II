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
        self.f_max = 0.75
        self.mu    = -999.

        # self._k = 1

    def pdf(self, x):
        # print self._k
        # self._k += 1
        return self.f_max*(1. - x**2.)

    def mean(self):
        a = self.x_min
        b = self.x_max

        self.mu = self.f_max*((0.5*b**2.) - (0.25*b**4.) - (0.5*a**2.) + (0.25*a**2.))
        return self.mu

    def std(self):
        if self.mu == -999.:
            self.mean()

        f0 = self.f_max * ((1./3.)*self.x_min**3. - (1./5.)*self.x_min**5.) - (2.*self.mu**2.) + (self.f_max*self.mu**2.)*(self.x_min - (1./3.)*(self.x_min**3.))
        f1 = self.f_max * ((1./3.)*self.x_max**3. - (1./5.)*self.x_max**5.) - (2.*self.mu**2.) + (self.f_max*self.mu**2.)*(self.x_max - (1./3.)*(self.x_max**3.))

        return np.sqrt(f1 - f0)

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
