####################################################################
# Otto: Perform Hypthothesis Testing
# M Pierce
# Created December 16, 2019
####################################################################

import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

##################################################################
# Get the Data
##################################################################

beforedata = np.array([4,6,4,5,6,4,6,5,4,5])
afterdata = np.array([7,6,5,6,7,4,6,6,6,5])

df = pd.read_csv("video-starts.csv") 
beforedata = np.array(df['Before'].values)
afterdata = np.array(df['After'].values)

##################################################################
# Calculate Stats
##################################################################
stat, p = ttest_ind(afterdata, beforedata, equal_var=False)

##################################################################
# Print Results to Screen
##################################################################

print("Otto: NBAD VOD Hyphothesis Testing")
print("============================")
print("")
print("Change: Limit Ad Duration based on Content Duration")
print("")
print("Null Hypothesis: VOD Starts/User Before Change = VOD Starts/User After Change")
print("Alternate Hypothesis: VOD Starts/User Before Change != VOD Starts/User After Change")
print("")
print("Two-tailed testing")
print("Significance Level: 0.05")
print(" ")
print("Samples")
print("=======")
print("Before: Starts/User/Day: "+str(beforedata))
print("Mean: "+str(beforedata.mean())+"     Std Dev: "+str(beforedata.std()) )
print("")
print("After: Starts/User/Day: "+str(afterdata))
print("Mean: "+str(afterdata.mean())+"     Std Dev: "+str(afterdata.std()) )
print("")
print("Calculations")
print('t-statistic=%.3f, p-value=%.3f' % (stat, p))
print("")
print("Test Conclusion")
if p > 0.05:
	print('   Null Hypothesis not rejected')
else:
    print('   Reject Null Hyphothesis')
    if stat > 0:
        print("     Change has positive effect on Starts/User")
    else:
        print("     Change has NEGATIVE effect on Starts/User")