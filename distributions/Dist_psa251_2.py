# -*- coding: utf-8 -*-

import numpy as np

import traceback

from .base_distribution import BaseDistribution

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
if __name__ == '__main__':
	test(Dist_psa251_2)
