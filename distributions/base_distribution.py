
import numpy as np

class BaseDistribution(object):
	def __init__(self):
		self.f_max = None
		self.x_min = None
		self.x_max = None

	def rvs(self, n_samples):
		"""This is going to call accept reject until we have enough samples"""
		acceptance_fraction = 1.
		temp = np.zeros(0)
		while temp.size<n_samples:
			#print n_samples, acceptance_fraction, n_samples/acceptance_fraction
			n_trys = np.int((n_samples-temp.size)/acceptance_fraction)
			new_samples = self.accept_reject(n_trys)
			if new_samples.size > 0:
				acceptance_fraction = 1.*new_samples.size/n_trys
			#print temp.shape, new_samples.shape
			temp = np.hstack((temp,new_samples))
		return temp[0:n_samples]

	def accept_reject(self, n_trys):
		"""This is the accept/reject algorithm we did in class"""
		x = np.random.uniform(self.x_min, self.x_max, n_trys)
		y = np.random.uniform(0, self.f_max, n_trys)
		accepted_x = []
		for i in range(n_trys):
		    if y[i] < self.pdf(x[i]):
		        accepted_x.append( x[i] ) 
		return np.array(accepted_x)


	def pdf(self, x):
		"""This is your PDF"""
		#print "not implemented"
		return np.abs(x)
        #raise NotImplementedError

	def mean(self):
		"""This is the mean of the PDF"""
		return 0.
        #raise NotImplementedError


	def std(self):
		"""This is the standard deviation of the pdf"""
		return np.sqrt(0.5)
        #raise NotImplementedError

