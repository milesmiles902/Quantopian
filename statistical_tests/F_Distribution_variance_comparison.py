#Compare two variances using the F-distrubution

import matplotlib.pyplot as plt
from scipy.stats import f

sym_list = ["SPY", "COHR"]
start_date = '2015-01-01'
end_date = '2017-07-10'
sample_price= get_pricing(sym_list, start_date = start_date, end_date = end_date, fields = 'price')
sample_price.columns = map(lambda x: x.symbol, sample_price.columns)
sample_returns = sample_price.pct_change()[1:]

sd_spy, sd_cohr = sample_returns.std() #sqrt(variance) = sqrt(sum[value-mean]**2/n)
print 'SPY standard deviation:', sd_spy
print 'COHR standard deviation:', sd_cohr

f_test = (sd_spy/sd_cohr)**2
print "F statistic: ", f_test

df_cohr = len(sample_returns['COHR'])-1
df_spy = len(sample_returns['SPY'])-1
print 'Degrees of freedom for SPY: ', df_cohr
print 'Degrees of freedom for COHR: ', df_spy

upper_crit_value = f.ppf(0.975, df_cohr, df_spy)
lower_crit_value = f.ppf(0.025, df_cohr, df_spy)
print 'Upper critical value at a = 0.05 with df_cohr = {0} and df_spy = {1}'.format(df_cohr, df_spy), upper_crit_value
print 'Lower critical value at a = 0.05 with df_cohr = {0} and df_spy = {1}'.format(df_cohr, df_spy), lower_crit_value
