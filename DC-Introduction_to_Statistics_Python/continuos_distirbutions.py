import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


##################
#Data back-ups
#The sales software used at your company is set to automatically back itself up,
#  but no one knows exactly what time the back-ups happen. It is known, however, 
# that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings
#  at random times to update the data on the client he just met with. He wants to know 
# how long he'll have to wait for his newly-entered data to get backed up. Use your new 
# knowledge of continuous uniform distributions to model this situation and 
# answer Amir's questions.
#####################

# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5,min_time,max_time) 

print(prob_less_than_5)


# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = 1 - uniform.cdf(5, min_time, max_time)
print(prob_greater_than_5)

# Calculate probability of waiting 10-20 mins
# prob_between_10_and_20 = (uniform.cdf(30,min_time,max_time) - ((1-uniform.cdf(20,min_time, max_time))+(uniform.cdf(10,min_time,max_time))))
prob_between_10_and_20 = ((uniform.cdf(20,min_time, max_time))-(uniform.cdf(10,min_time,max_time)))
print(prob_between_10_and_20)


##################
#Simulating wait times
#To give Amir a better idea of how long he'll have to wait, you'll simulate Amir 
# waiting 1000 times and create a histogram to show him what he should expect. Recall
#  from the last exercise that his minimum wait time is 0 minutes and his maximum wait
#  time is 30 minutes.
#####################

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()