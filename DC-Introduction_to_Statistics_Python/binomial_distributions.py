import numpy as np

##################
#Simulating sales deals
#Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals
#  he works on. Each deal has a binary outcome: it's either lost, or won, so you can 
# model his sales deals with a binomial distribution. In this exercise, you'll help Amir 
# simulate a year's worth of his deals so he can better understand his performance.
#####################

from scipy.stats import binom

np.random.seed(10)

# Simulate a single deal (1 win, 0 loss)
print(binom.rvs(1, 0.30, size=1))

# Simulate 1 week of 3 deals
print(binom.rvs(3,0.30,size=1))

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.30,size=52)

# Print mean deals won per week
print(deals)
print(np.mean(deals))



##################
#Calculating binomial probabilities
#Just as in the last exercise, assume that Amir wins 30% of deals. He wants to get an 
# idea of how likely he is to close a certain number of deals each week. In this exercise,
#  you'll calculate what the chances are of him closing different numbers of deals using
# the binomial distribution.
#####################

#What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
prob_3 = binom.pmf(3,3,0.30)

#What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.
prob_less_than_or_equal_1 = binom.cdf(1,3,0.30)

#What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.
prob_greater_than_1 = 1 - binom.cdf(1,3,0.30)


##################
#How many sales will be won?
#Now Amir wants to know how many deals he can expect to close each week if his win rate 
# changes. Luckily, you can use your binomial distribution knowledge to help him calculate
# the expected value in different situations. Recall from the video that the expected 
# value of a binomial distribution can be calculated by nxp
#####################

#Calculate the expected number of sales out of the 3 he works on that Amir will win each
#  week if he maintains his n% win rate.



# Expected number won with 30% win rate
won_30pct = 3 * 0.30
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)




