
import numpy as np
from .base_distribution import BaseDistribution

class Dist_kc90(BaseDistribution):
	def __init__(self):
		self.f_max = 1
		self.x_min = 0
		self.x_max = 1


	def pdf(self, x):
		##Accept Recj I
        import numpy as np
        import matplotlib.pyplot as plt
        def f(x):
            y = np.fabs(x)
            return y
        def f2(z):
            f_list = []
            if z>0
                for a in range (z, np.fabs(z)):
                    b = np.fabs(a)
                    f_list.append(b)
            else
                for a in range ((-z), z):
                    b = a
                    f_list.append(b)
            return f_list
        def acceptReject(N):
            aR_list = []
                for a in range (0, N):
                    b = np.random.rand
                    if (0<=np.fabs(b)<=1):
                        aR_list.append(b)
                        a = (a+1)
                    else:
                        a = (a+1)
                        aR_list.append(b)
            return aR_list
        def makePlots(N):
            acceptReject(N)
            accept_prob = aR_list.size/N
            f2(N)
            np.mean (aR_list)
            np.std (aR_list)
            plt.hist(aR_list, bins=100)
            plt.hist(f_list, bins=100)
            plt.show
        makePlots(100)
        makePlots(1000)
        makePlots(10000)
        ##Accept Reject II
        def acceptReject2(N):
            aR2_list = []
            while len(aR2_list)<N:
                for a in range (0, N):
                    b = np.random.rand
                    if (0<=np.fabs(b)<=1):
                        aR_list.append(b)
                        a = (a+1)
                    else:
                        a = (a+1)
            return aR2_list
        ##Central Limit Theorem I
        def acceptReject3(M):
        aR3_list = []
        for a in range (0,M):
        acceptReject(2)
        s=np.sum(aR2_list)
        aR3_list.append(s)
        return aR3_list
        plt.hist(s, normed=1)
		return 1.
