
'''

The idea is to take the observation x of random variable X, and transform x st its mean and median are approximately equal, thus the difference test can be applied to test for equal medians.


'''

import numpy as np
np.random.seed(1)
n = 100
x = np.random.exponential(1,n)
print('mean x',np.mean(x))
# mean x 0.9482394982391559
print('median x',np.median(x))
# median x 0.6370556013874097

# Okay, they're pretty different. Now consider:

y = (x+np.flip(x))/2
print('mean y',np.mean(y))
# mean y 0.9482394982391557
print('median y',np.median(y))
# median y 0.8025240349335689

# Much closer. I think this is essentially the CLT. Should get the same by doing a random shuffle of x and adding to to x.

v = x.copy()
np.random.shuffle(v)
y = (x+v)/2
print('mean y',np.mean(y))
# mean y 0.9482394982391557
print('median y',np.median(y))
# mean y 0.9482394982391555
# median y 0.7776963763290787

# About the same as the last method, notice the mean hasn't been changed. 
y = (x+v+np.flip(x))/3
print('mean y',np.mean(y))
# mean y 0.9482394982391555
print('median y',np.median(y))
# median y 0.8261393465006637

# A bit better yet. Now lets go wild with it:

y = x+np.flip(x)
N = n//10
for n in range(N):
    v = x.copy()
    np.random.shuffle(v)
    y = y+v
y = y/(N+2)

print('mean y',np.mean(y))
print('median y',np.median(y))
# mean y 0.9482394982391557
# median y 0.9174383982326322

# Notice the mean is still the mean of x (with some numerical error), but the median is much closer to the mean than the median of x. Again, I believe this is basically the CLT.