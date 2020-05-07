import numpy as np
from .base_distribution import BaseDistribution

class Dist_hy1660(BaseDistribution):
   def __init__(self):
      self.f_max = 2
      self.x_min = 0
      self.x_max = 1


   def pdf(self, x):
      """This is your PDF"""
      return 2*x

   def mean(self):
      """This is the mean of the PDF"""
      return 2/3 #Mean of x is 2/3

   def std(self):
      """This is the standard deviation of the pdf"""
      return np.sqrt(1/18) #The variance of the pdf is 1/18