#Pearson chi squared test
#251 trading days per year

from scipy.stats import chi2
import matplotlib.pyplot as plt

sym_list = ["COHR"]
start_date = '2015-01-01'
end_date = '2017-07-10'
sample_price= get_pricing(sym_list, start_date = start_date, end_date = end_date, fields = 'price')
sample_returns = sample_price.pct_change()[1:]
plt.plot(sample_returns.index, sample_returns.values)
plt.ylabel('Returns');

sd_cohr = sample_returns.std()
chi_test = ((len(sample_returns)-1)*sd_cohr)**2 /0.0001
print 'Chi-squared test', chi_test

##As compared to the critical value
crit_value = chi2.ppf(0.99, len(sample_returns)-1)
print 'Critical value: 0.01 with 251 df (days trading per year)', crit_value
