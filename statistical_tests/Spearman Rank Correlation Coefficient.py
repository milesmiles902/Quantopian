###Spearman Rank Correlation Coefficient

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as pyplot
import math

def compare_correlation_and_spearman_rank(X, Y):
    
	X_rank = stats.rankdata(X, method='average')
	Y_rank = stats.rankdata(Y, method='average')
	n = len(X_rank)

	diff = X_rank-Y_rank

	spear_corr = 1-6*sum(diff**2)/(n*(n**2 -1))
	norm_corr = np.corrcoef(X, Y)[0,1]

	return spear_corr, norm_corr

###Example: SPY vs COHR
cohr = get_pricing('COHR',fields = 'price', start_date='2016-10-17', end_date='2016-10-25', frequency = 'daily').pct_change()[1:]
spy = get_pricing('SPY',fields = 'price', start_date='2016-10-17', end_date='2016-10-25', frequency = 'daily').pct_change()[1:]

print compare_correlation_and_spearman_rank(cohr, spy)

###Alternative method
print stats.spearmanr(cohr, spy)