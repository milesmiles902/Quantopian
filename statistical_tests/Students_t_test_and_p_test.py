#Student's t-test on a sample
#P-tes
#Null hypothesis: That the mean return is significantly greater than zero.

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t

sym_list = ["COHR"]
start_date = '2015-01-01'
end_date = '2017-07-10'
sample_price= get_pricing(sym_list, start_date = start_date, end_date = end_date, fields = 'price')
sample_price.columns = map(lambda x: x.symbol, sample_price.columns)
sample_returns = sample_price.pct_change()[1:]
sample_returns.plot()
plt.ylabel('Returns');

mean_cohr = sample_returns.mean()
sd_cohr = sample_returns.std() #sqrt(variance) = sqrt(sum[value-mean]**2/n)
n_cohr = len(sample_returns['COHR'])

t_test = (mean_cohr-0)/sd_cohr/np.sqrt(n_cohr)
p_test = 2*(1-t.cdf(t_test, n-1)) #CDF=cumulative distrubtion function of t-test
print 't-test', t_test
print 'p-value', p_test