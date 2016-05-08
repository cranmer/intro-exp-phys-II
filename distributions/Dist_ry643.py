import numpy as np
from .base_distribution import BaseDistribution

class Dist_ry643(BaseDistribution):
    def __init__(self):
        self.f_max = 2
        self.x_min = 0
        self.x_max = 2


    def pdf(self, x):
        """This is your PDF"""
        return (x**3)/4

    def mean(self):
        """This is the mean of the PDF"""
        return 8./5 #integral (from self.x_min to self.x_max) of x times f(x)
<<<<<<< HEAD:Dist_ry643.py
=======
        		# (((self.x_max)**5)/20) - (((self.x_min)**5)/20)
>>>>>>> cranmer/master:distributions/Dist_ry643.py

    def std(self):
        """This is the standard deviation of the pdf"""
        return np.sqrt(8./75)    #integral (from self.x_min to self.x_max) of [(x-mean)**2 times f(x)]
                                 #sqrt of answer gives std dev.
<<<<<<< HEAD:Dist_ry643.py
=======
                                 # np.sqrt(((1875*(self.x_max**6) - 480*(self.x_max**5) + 32*(self.x_max**4))/45000) - ((1875*(self.x_min**6) - 480*(self.x_min**5) + 32*(self.x_min**4))/45000))
>>>>>>> cranmer/master:distributions/Dist_ry643.py
        
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
	test(Dist_ry643)
