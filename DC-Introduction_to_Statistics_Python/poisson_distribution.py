#############
#Tracking lead responses
#Your company uses sales software to keep track of new sales leads. It organizes them 
#into a queue so that anyone can follow up on one when they have a bit of free time. 
#Since the number of lead responses is a countable outcome over a period of time, this 
#scenario corresponds to a Poisson distribution. On average, Amir responds to 4 leads 
#each day. In this exercise, you'll calculate probabilities of Amir responding to 
#different numbers of leads.
###############

# Import poisson from scipy.stats
from scipy.stats import poisson

# Probability of 5 responses
prob_5 = poisson.pmf(5,4)

print(prob_5)

#Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?

# Probability of 5 responses
prob_coworker = poisson.pmf(5,5.5)

print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2,4)

print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1 - poisson.cdf(10,4)

print(prob_over_10)


