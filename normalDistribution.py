####################################################################
# Otto: Plot Normal Distribution and Histogram
# M Pierce
# Created December 22, 2019
####################################################################

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

##################################################################
# Get the Data
##################################################################

# beforedata = np.array([4,6,4,5,6,4,6,5,4,5,4,6,4,5,6,4,6,5,4,5])
# afterdata = np.array([7,6,5,6,7,4,6,6,6,5,7,6,5,6,7,4,6,6,6,5])
df = pd.read_csv("video-starts.csv") 
beforedata = np.array(df['Before'].values)
afterdata = np.array(df['After'].values)

##################################################################
# Calculate Stats
##################################################################

mu = beforedata.mean()
sigma = beforedata.std()

mu2 = afterdata.mean()
sigma2 = afterdata.std()

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)[source]
#     Return evenly spaced numbers over a specified interval.
a = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
b = np.linspace(mu2 - 3*sigma2, mu2 + 3*sigma2, 100)

##################################################################
# Plot the Data
##################################################################

fig, ax = plt.subplots(1, 2)  #subplot(nrows, ncols, index, **kwargs)

ax[0].plot(a, stats.norm.pdf(a, mu, sigma), label="Before")
ax[0].plot(b, stats.norm.pdf(b, mu2, sigma2), label="After")
ax[0].title.set_text(r'$\mu_1=$'+str(mu)+' vs '+r'$\mu_2=$'+str(mu2))
ax[0].legend(loc='best')
ax[0].set_xlabel("Video Starts")
ax[0].set_ylabel("Probability")

# ax[1].plot(b, stats.norm.pdf(b, mu2, sigma2), label="After")
ax[1].hist(beforedata,label="Before", histtype='step', density=False)
ax[1].hist(afterdata,label="After", histtype='step', density=False)
ax[1].title.set_text('Histogram')
ax[1].legend(loc='best')
ax[1].set_xlabel("Video Starts")
ax[1].set_ylabel("Frequency")

fig.suptitle("Michael's Python Graphicization")
# fig.tight_layout()

plt.savefig("mpgraph-dist.png")