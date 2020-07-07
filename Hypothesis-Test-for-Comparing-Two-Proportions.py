#Hypothesis Test for Comparing Two Proportions

#Libraries
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

#Null Hypothesis: The difference in proportions is = 0.  HA: the difference in proportions is ≠ 0.
Ho = 0

#Number of users converted in each campaign
conv_users = np.array([220, 280])

#Total number of users in each campaign
t_users = np.array([4530, 5234])

#Two-sided hypothesis test
z_stat, p_val = proportions_ztest(conv_users, t_users, value = Ho, alternative='two-sided', prop_var=False)

#Test Statistic
print('Test Statistic:','{0:0.4f}'.format(z_stat))

#P-value
print('P-value :','{0:0.4f}'.format(p_val))

#Results
alpha = 0.1

if p_val < alpha:
   print("Statistically significant, reject null hypothesis that population proportions are equal")
else:
  print("Not significant, fail to reject the null hypothesis that population proportions are equal")
