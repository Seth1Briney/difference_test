# sign_test
Using Python to look at the statistical difference test as described in chapter 14 of Mathematical Statistics - 7th Edition - Mendenhall, Wackerly, Scheaffer

The difference test takes the difference of two vector observations x, y of two random variables X, Y and creates a Binomial variable Z which is the count of pairwise observations where x>y. (or should it be pairwise observations in the cartesian product { (x_i, y_i) | x_i in x, y_i in y }?), I suppose the Cartesian product version would be superior especially for small sample size because by observations I mean iid, thus there is no significance to the ordering of x or y.

Anyway, in Python I would say:
z = np.sum(x>y)

Then z is the observation of a Binomial random variable, which under H0: median(X)=median(Y), Z~B(n,1/2) in expectation. Z can be used to test if X and Y have the same distribution, or more generally have the same median.

By the central convergence theorem (Introduction to Mathematical Statistics, Hogg; Dr. Kimihiro Noguchi WWU) we can "unskew" data by averaging it with ts shuffled values (Dr. Ramadha Piyadi Gamage, WWU), thus the sign test can be applied to testing for equivalent means too. This averaged shuffling can be done repeatedly, but clearly if done too many times will converge to the constant mean vector, so probably should be limited by some fraction of the number of observations, I conject. Maybe n/10 times, for example.

This brings the question of whether in the context of testing for equal means the sign test has any advantages over Student's T-test, and when these advantages may arise. Especially considering the method of averaged shuffling of the data makes the data closer to normal, thus more compatible with the T-test.

Of course, the sign test is used more generally in non-parametric testing of equal distributions, and not as far as I can see intended to replace Student's T-test.
