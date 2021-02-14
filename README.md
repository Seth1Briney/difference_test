# sign_test
Using Python to look at the statistical difference test as described in chapter 14 of Mathematical Statistics - 7th Edition - Mendenhall, Wackerly, Scheaffer

The difference test takes the difference of two vector observations x, y of two random variables X, Y and creates a Binomial variable Z which is the count of pairwise observations where x>y. (or should it be pairwise observations in the cartesian product { (x_i, y_i) | x_i in x, y_i in y }?), I suppose the Cartesian product version would be superior especially for small sample size because by observations I mean iid, thus there is no significance to the ordering of x or y.

Anyway, in Python I would say:
z = np.sum(x>y)

Then z is the observation of a Binomial random variable, which under H0: median(X)=median(Y), Z~B(n,1/2) in expectation. Z can be used to test if X and Y have the same distribution, or more generally have the same median.

By the central convergence theorem (Introduction to Mathematical Statistics, Hogg; Dr. Kimihiro Noguchi WWU) we can "unskew" data by averaging it with ts shuffled values (Dr. Ramadha Piyadi Gamage, WWU), thus the sign test can be applied to testing for equivalent means too.
