#Welch's t-test on two samples with unequal variances i.e. two stocks
#Alternative hypothesis: That the difference of means is significantly greater than zero.

import matplotlib.pyplot as plt

sym_list = ["SPY", "COHR"]
start_date = '2015-01-01'
end_date = '2017-07-10'
sample_price= get_pricing(sym_list, start_date = start_date, end_date = end_date, fields = 'price')
sample_price.columns = map(lambda x: x.symbol, sample_price.columns)
sample_returns = sample_price.pct_change()[1:]
sample_returns.plot()
plt.ylabel('Returns');

mean_spy, mean_cohr = sample_returns.mean()
sd_spy, sd_cohr = sample_returns.std() #sqrt(variance) = sqrt(sum[value-mean]**2/n)
n_spy = len(sample_returns['SPY'])
n_cohr = len(sample_returns['COHR'])

t_test = ((mean_spy-mean_cohr)-0)/((sd_spy**2/n_spy) + (sd_cohr**2/n_cohr))**0.5
df = ((sd_spy**2/n_spy) + (sd_cohr**2/n_cohr))**2/(((sd_spy**2/n_spy)/n_spy) +((sd_cohr**2/n_cohr)**2/n_cohr))

print 't-test', t_test
print 'Degrees of freedom', df