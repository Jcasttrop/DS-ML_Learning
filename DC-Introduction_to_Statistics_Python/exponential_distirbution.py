#############
"Modeling time between leads
"To further evaluate Amir's performance, you want to know how much time it takes
#him to respond to a lead after he opens it. On average, he responds to 1 request every 
# 2.5 hours. In this exercise, you'll calculate probabilities of different amounts of time
#  passing between Amir receiving a lead and sending a response.
#############

# Import expon from scipy.stats
from scipy.stats import expon

# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1-expon.cdf(4,scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(3,scale=2.5) - expon.cdf(4,scale=2.5))

