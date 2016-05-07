# -*- coding: utf-8 -*-

import numpy as np

import traceback

from .base_distribution import BaseDistribution

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
if __name__ == '__main__':
    test(Dist_psa251)
