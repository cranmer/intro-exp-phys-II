
import numpy as np
from .base_distribution import BaseDistribution

class Dist_kc90(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		# “def f(x):” that returns the absolute value of x.
import matplotlib.pyplot as plt
import numpy as np


# “def f(x):” that returns the absolute value of x.
def f(x):
    return abs(x)


# “def acceptReject(N):” that returns a list of accepted {xi} using the accept / reject
# algorithm

def acceptReject(N):
    result = []
    for _ in range(N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(0, 1)
        if y < f(x):
            result.append(x)
    return np.array(result)


# “def makePlots():” that will for N=100, 1,000, and 100,000 do the following: a) call
# acceptReject(N), b) calculate the acceptance efficiency, c) calculate the mean and
# standard deviation for the {xi} , d) make a normalized histogram of {xi}, and e)
# overlay the function f(x).
def makePlots():
    N_list = [100, 1000, 100000]
    for N in N_list:
        # a) call acceptReject(N),
        result = acceptReject(N)
        accepted_len = len(result)
        # b) calculate the acceptance efficiency,
        efficiency = accepted_len / N
        # c) calculate the mean and standard deviation for the {xi}
        mean = result.mean()
        sd = result.std()
        # d) make a normalized histogram of {xi}, and
        plt.hist(result, normed=True, bins='auto')
        # e) overlay the function f(x)
        # 3. clearly label cells in your notebook that has plots for N=100, 1,000, and 100,000.
        # 4. note the mean, standard deviation, and acceptance efficiency for your three plots.
        plt.title(
            "f(x)=|x|, (N={}), \nmean:{}, \nstandard deviation:{}, \nacceptance efficiency:{}".format(
                N, mean, sd, efficiency))
        plt.show()


# Create a new cell defining a new acceptReject(N) function.
def newAcceptReject(N):
    result = []
    while (len(result) < N):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(0, 1)
        if y < f(x):
            result.append(x)
    return np.array(result)


makePlots()

#Central Limit Theorem I 
 
def acceptReject3(M):     
    aR3_list = []     
    for a in range (0,M):         
        acceptReject(2)         
        s=np.sum(aR2_list)        
        aR3_list.append(s)     
      return aR3_list 
 
plt.hist(s, normed=1) 
		return 1.
