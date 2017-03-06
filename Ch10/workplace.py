# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:15:10 2017

@author: zhaox
"""

import kMeans
import matplotlib
import matplotlib.pyplot as plt

from numpy import *

datMat=mat(kMeans.loadDataSet('testSet2.txt'))

myCentroids, myNewAssments=kMeans.kMeans(datMat,3)


plt.scatter(datMat[:,0],datMat[:,1])
plt.scatter(myCentroids[:,0],myCentroids[:,1],marker='+',color='r')
