#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:22:39 2019

@author: compsci
"""




import random
import os
import math
import pandas as pd
from pandas import Series
from statistics import mean
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import rcParams
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter
from sklearn.preprocessing import PolynomialFeatures
import csv
import seaborn as sb


data_project = pd.read_csv('python_data.csv', sep = ',', names = ['State', 'GDP2012', 'GDP2013', 'GDP2014', 'GDP2015', 'GDP2016', 'DYX2012', 'DYX2013', 'DYX2014', 'DYX2015', 'DYX2016'], index_col = ['State'])

x = data_project['GDP2012']
y = data_project['DYX2012']
m= ((x.mean()*y.mean()) - x.mean()*y.mean() /
         ((x.mean()*x.mean())) - (x * x).mean())
b= y.mean() - m * x.mean()
regression_line = []

for xs in x:
    regression_line.append((m*xs)+b)
plt.style.use('ggplot')
plt.scatter(x.values,y.values, color = 'r')
plt.xlabel("GDP Per Capita of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.title("GDP Per Capita vs. Dyslexia rates 2012")
plt.axis([10000,3000000,0,7.5])
plt.plot(x, regression_line, color = 'r')
plt.show()


#_____________________________________________________________________________
x = data_project['GDP2013']
y = data_project['DYX2013']
m= ((x.mean()*y.mean()) - x.mean()*y.mean() /
         ((x.mean()*x.mean())) - (x * x).mean())
b= y.mean() - m * x.mean()
regression_line = []
for xs in x:
    regression_line.append((m*xs)+b)
plt.style.use('ggplot')
plt.scatter(x.values,y.values, color = 'g')
plt.xlabel("GDP Per Capita of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.title("GDP Per Capita vs. Dyslexia rates 2013")
plt.axis([10000,3000000,0,7.5])
plt.plot(x, regression_line, color = 'g')
plt.show()



x = data_project['GDP2014']
y = data_project['DYX2014']
m= ((x.mean()*y.mean()) - x.mean()*y.mean() /
         ((x.mean()*x.mean())) - (x * x).mean())
b= y.mean() - m * x.mean()
regression_line = []
for xs in x:
    regression_line.append((m*xs)+b)
plt.style.use('ggplot')
plt.scatter(x.values,y.values, color = 'b')
plt.xlabel("GDP Per Capita of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.title("GDP Per Capita vs. Dyslexia rates 2014")
plt.axis([10000,3000000,0, 7.5])
plt.plot(x, regression_line, color = 'b')
plt.show()



x = data_project['GDP2015']
y = data_project['DYX2015']
m= ((x.mean()*y.mean()) - x.mean()*y.mean() /
         ((x.mean()*x.mean())) - (x * x).mean())
b= y.mean() - m * x.mean()
regression_line = []
for xs in x:
    regression_line.append((m*xs)+b)
plt.style.use('ggplot')
plt.scatter(x.values,y.values, color = 'y')
plt.xlabel("GDP Per Capita  of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.title("GDP Per Capita vs. Dyslexia rates 2015")
plt.axis([10000,3000000,0,7.5])
plt.plot(x, regression_line, color = 'y')
plt.show()



x = data_project['GDP2016']
y = data_project['DYX2016']
m= ((x.mean()*y.mean()) - x.mean()*y.mean() /
         ((x.mean()*x.mean())) - (x * x).mean())
b= y.mean() - m * x.mean()
regression_line = []
for xs in x:
    regression_line.append((m*xs)+b)
plt.style.use('ggplot')
plt.scatter(x.values,y.values, color = 'm')
plt.xlabel("GDP Per Capita of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.title("GDP Per Capita vs. Dyslexia rates 2016")
plt.axis([10000,3000000,0,7.5])
plt.plot(x, regression_line, color= 'm')
plt.show()


#all on one plot_____________________________________________

x2012 = data_project['GDP2012']
y2012 = data_project['DYX2012']
m2012 = ((x2012.mean()*y2012.mean()) - x2012.mean()*y2012.mean() /
         ((x2012.mean()*x2012.mean())) - (x2012 * x2012).mean())
b2012 = y2012.mean() - m2012 * x2012.mean()
regression_line2012 = []
#2012_________________________________________________________
x2013 = data_project['GDP2013']
y2013 = data_project['DYX2013']
m2013= ((x2013.mean()*y2013.mean()) - x2013.mean()*y2013.mean() /
         ((x2013.mean()*x2013.mean())) - (x2013 * x2013).mean())
b2013= y2013.mean() - m2013 * x2013.mean()
regression_line2013 = []
#2013__________________________________________________________
x2014 = data_project['GDP2014']
y2014 = data_project['DYX2014']
m2014= ((x2014.mean()*y2014.mean()) - x2014.mean()*y2014.mean() /
         ((x2014.mean()*x2014.mean())) - (x2014 * x2014).mean())
b2014= y2014.mean() - m2014 * x2013.mean()
regression_line2014 = []
#2014_________________________________________________________
x2015 = data_project['GDP2015']
y2015 = data_project['DYX2015']
m2015= ((x2015.mean()*y2015.mean()) - x2015.mean()*y2015.mean() /
         ((x2015.mean()*x2015.mean())) - (x2015 * x2015).mean())
b2015= y2015.mean() - m2015 * x2015.mean()
regression_line2015 = []
#2015________________________________________________________
x2016 = data_project['GDP2016']
y2016 = data_project['DYX2016']
m2016= ((x2016.mean()*y2016.mean()) - x2016.mean()*y2016.mean() /
         ((x2016.mean()*x2016.mean())) - (x2016 * x2016).mean())
b2016= y2016.mean() - m2016 * x2016.mean()
regression_line2016 = []
for xs in x:
    regression_line2012.append((m2012*xs)+b2012)
    regression_line2013.append((m2013*xs)+b2013)
    regression_line2014.append((m2014*xs)+b2014)
    regression_line2015.append((m2015*xs)+b2015)
    regression_line2016.append((m2016*xs)+b2016)
plt.style.use('ggplot')

plt.scatter(x2012.values,y2012.values, color = 'r', label = '2012')
plt.scatter(x2013.values,y2013.values, color = 'g', label = '2013')
plt.scatter(x2014.values,y2014.values, color = 'b', label = '2014')
plt.scatter(x2015.values,y2015.values, color = 'y', label = '2015')
plt.scatter(x2016.values,y2016.values, color = 'm', label = '2016')

plt.xlabel("GDP Per Capita of Each State")
plt.ylabel("Dyslexia rate of each state")
plt.legend()
plt.title("GDP Per Capita vs. Dyslexia rates 2012-2016")
plt.axis([10000 ,3000000, 0, 7.5])
plt.plot(x2012, regression_line2012, color = 'r')
plt.plot(x2013, regression_line2013, color = 'g')
plt.plot(x2014, regression_line2014, color = 'b')
plt.plot(x2015, regression_line2015, color = 'y')
plt.plot(x2016, regression_line2016, color = 'm')
plt.show()





























