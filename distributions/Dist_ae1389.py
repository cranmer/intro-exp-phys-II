import numpy as np
from base_distribution import BaseDistribution

class Dist_ae1389(BaseDistribution):
  def __init__(self):
     self.f_max = np.sin(np.pi*np.cos(x**2))
     self.x_min = 0
     self.x_max = 60


  def pdf(self, x):
     """This is your PDF"""
     return np.sqrt(np.sec(x**4))

  def mean(self):
     """This is the mean of the PDF"""
     return np.pi

  def std(self):
     """This is the standard deviation of the pdf"""
     return (np.pi/10)
