'''

Compare T-test vs Binomial difference test for comparing means for symmetric distributions.

The difference test takes the vector difference of observations of two random variables, and checks how many of the differences are positive. The result is binomial and is maximized when the medians are equal. This is a test for determining of medians are equal, or if two variables come from the same distribution.

Now say X is a random variable, and is not symmetric so E[X]!=median(X). Consider the observation x, and let:

z = (x+reverse(x))/2.
E[z]=E[x] by linearity, but the median will be closer to the mean than with x.

In fact, we can do many shufflings of x and average them without changing the mean. Of course, doing this too many times will make all the observations the same.

'''

import numpy as np
from numpy import sqrt
from numpy.random import randn
np.random.seed(1)
from scipy.stats import norm, binom, ttest_ind

def ceil(x):
    if int(x)<x: return int(x)+1
    else: return x

for n in [10,100,1000,10000]:

    print('\nn',n)
    mux = 0
    print('mux',mux)
    xs = mux+randn(n,1)
    ys = randn(n,1)

    for shift_y in [0,1,2,3,4]:
        muy = mux + shift_y
        print('muy',muy)
        ys_tmp = ys+muy

        # H0: (x-y)/sqrt(2)~N(0,1).
        # Ha: (x-y)/sqrt(2)~N(mu,1), mu!=0.

        s = np.sqrt( np.var(xs) + np.var(ys_tmp) )
        t = np.mean( np.sqrt(n)*(xs-ys_tmp)/s )
        pval = 2*norm.cdf( -np.abs(t) )
        print('norm cdf pval:',pval)
        pval = ttest_ind(xs, ys_tmp, axis=0, equal_var=True, nan_policy='propagate')[-1][0]
        print('ttest pval:',pval)
        # Now consider the following variable z, note under the assumption of equal medians z~B(n,0.5), but in the case of symmetric distributions such as those under consideration equal medians is equivalent to equal means H0:
        z = np.sum(xs>ys_tmp)
        if z>n/2: z = n-z # print(binom.cdf(10-8,10,0.5)-(binom.pmf(8,10,.5)+binom.pmf(9,10,.5)+binom.pmf(10,10,.5))) # # 1.3877787807814457e-17
        pval = 2*binom.cdf(z,n,0.5)
        pval = min(pval,1)
        print('binomial difference pval:',pval)

# n 10
# mux 0
# muy 0
# norm cdf pval: 0.8828348704060637
# ttest pval: 0.8903598237675886
# binomial difference pval: 1
# muy 1
# norm cdf pval: 0.059177025304570266
# ttest pval: 0.09028280113864379
# binomial difference pval: 0.10937500000000003
# muy 2
# norm cdf pval: 8.813535909153114e-05
# ttest pval: 0.0015675826297873122
# binomial difference pval: 0.001953125
# muy 3
# norm cdf pval: 2.594673979143944e-09
# ttest pval: 2.3271157153406907e-05
# binomial difference pval: 0.001953125
# muy 4
# norm cdf pval: 1.3534120326417438e-15
# ttest pval: 5.24030289971797e-07
# binomial difference pval: 0.001953125

# n 100
# mux 0
# muy 0
# norm cdf pval: 0.5726181636420529
# ttest pval: 0.5751789736962398
# binomial difference pval: 0.36820161732669654
# muy 1
# norm cdf pval: 1.1591591702176593e-16
# ttest pval: 2.2444815309155262e-14
# binomial difference pval: 2.7027625220487873e-10
# muy 2
# norm cdf pval: 1.083541832927306e-57
# ttest pval: 2.5710634502626083e-37
# binomial difference pval: 1.2523245125385358e-22
# muy 3
# norm cdf pval: 1.6348411519740848e-124
# ttest pval: 1.7184995817673799e-59
# binomial difference pval: 1.5777218104420236e-30
# muy 4
# norm cdf pval: 3.4399504151314328e-217
# ttest pval: 1.359806590549739e-78
# binomial difference pval: 1.5777218104420236e-30

# n 1000
# mux 0
# muy 0
# norm cdf pval: 0.7848720448579455
# ttest pval: 0.7850051872762
# binomial difference pval: 0.9747749818223166
# muy 1
# norm cdf pval: 2.8969880230058552e-112
# ttest pval: 3.7773299215457177e-100
# binomial difference pval: 5.3563574362482685e-62
# muy 2
# norm cdf pval: 0.0
# ttest pval: 2.034277970161221e-303
# binomial difference pval: 4.751085930229918e-187
# muy 3
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 3.691642519328982e-274
# muy 4
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 1.8665272370064378e-301

# n 10000
# mux 0
# muy 0
# norm cdf pval: 0.4387836927077069
# ttest pval: 0.43881573487656944
# binomial difference pval: 0.502859752200474
# muy 1
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 0.0
# muy 2
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 0.0
# muy 3
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 0.0
# muy 4
# norm cdf pval: 0.0
# ttest pval: 0.0
# binomial difference pval: 0.0
