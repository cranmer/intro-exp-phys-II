import numpy as np
from .base_distribution import BaseDistribution

class Dist_sdl433(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = -1
		self.x_max = 1
        self.f = np.array([])
        self.domain = np.array([])

    #Exponential distribution starting at x in [0,1]
    #Takes in x as an array
	def pdf(self, x):

        #Define the domain
        x_min = 0
        x_max = 1
        domain = np.linspace(x_min, x_max, num = 10000)

        #Define exponential function
        f = 10 * np.e ** (-10 * x)

        #Calculate distribution function at x
        f_of_x = f[x * 10000]

        #Integrate
        Z = np.trapz(f, x, dx = 1/10000)

        return f_of_x / Z

	def mean(self):
        """This is the mean of the pdf"""
		return np.trapz(
            domain * pdf(domain),
            domain,
            dx = 1/10000
            )

	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(
            np.trapz(
                pdf(domain) * (domain - mean) ** 2),
                domain,
                dx = 1/10000
                )
            )
