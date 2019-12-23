####################################################################
# Otto: Linear Regression and Plot
# M Pierce
# Created December 10, 2019
####################################################################

import numpy as np
from numpy.polynomial.polynomial import polyfit
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

##################################################################
# Get the Data
##################################################################

# x = np.random.randint(low=1, high=100, size=10)
# y = np.random.randint(low=1, high=100, size=10)
# x = np.array([75667,14178,65586,7344,68206,8075])
# y = np.array([1099199,350117,880793,157383,1202017,215152])
df = pd.read_csv("tntot-stats-ytd.csv") 
x = np.array(df['Pre-Roll'].values)
y = np.array(df['Mid-Roll'].values)

##################################################################
# Calculate Statistics
##################################################################

# Compare Numpy to Stats Library

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# Fit with polyfit
b, m = polyfit(x, y, 1)

print (slope, intercept, r_value, p_value)
# print ("poly: "+str(m))

##################################################################
# Plot the Data
##################################################################

plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')

plt.title("Otto: Python Regression: Do TNTOT Pre-Rolls predict Midrolls?")
plt.xlabel('Prerolls')
plt.ylabel('Midrolls')
plt.text(2000, 160000,'Slope: '+str(round(slope,3)), ha='left', va='center')
plt.text(2000, 150000,'Intercept: '+str(round(intercept,3)), ha='left', va='center')
plt.text(2000, 140000,'R-squared: '+str(round(r_value,3)), ha='left', va='center')
plt.text(2000, 130000,'P-value: '+str(round(p_value,5)), ha='left', va='center')

plt.text(12000,60000, 'NBA.com TNTOT Desktop')
plt.text(12000,50000, 'Season-to-date')

# plt.annotate('>95%', xy=(30000, 1000000),  xycoords='data',
#             xytext=(0.6, 0.75), textcoords='axes fraction',
#             arrowprops=dict(facecolor='red', shrink=0.05),
#             horizontalalignment='right', verticalalignment='top',
#             )

# plt.show()  Need tkinter to have interactive
plt.savefig("mpgraph-linear.png")