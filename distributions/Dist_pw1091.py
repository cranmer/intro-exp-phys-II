
import numpy as np
from .base_distribution import BaseDistribution

class Dist_pw1091(BaseDistribution):
    def __init__(self):
        self.f_max = 1
        self.x_min = -(3./2.)**(1/3)
        self.x_max = (3./2.)**(1/3)


    def pdf(self, x):
        return x**2.

    def mean(self):
        return 0.

    def std(self):
        return 0.88669