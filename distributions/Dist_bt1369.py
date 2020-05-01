import numpy as np
from .base_distribution import BaseDistribution

class Dist_bt1369(BaseDistribution):
    def __init__(self):
        self.f_max = 0.22215
        self.x_min = 0.86289
        self.x_max = 8.44000

    def pdf(self, x):
        return 0.00029485724*x**4-0.00766628834*x**3+0.04983087421*x**2-0.05336916114*x+0.01371086184

    def mean(self):
        return 5.105308322606092

    def std(self):
        return 1.56953460038
