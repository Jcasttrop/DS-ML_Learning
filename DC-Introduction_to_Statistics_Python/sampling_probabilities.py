import pandas as pd
import numpy as np

amir_deals = pd.read_csv('C:\Users\Julian.Castro\Desktop\DS-ML_Learning\DC-Introduction_to_Statistics_Python\amir_deals.csv')

#############################################
#Calculating probabilities
#You're in charge of the sales team, and it's time for performance reviews, 
# starting with Amir. As part of the review, you want to randomly select a few of the
#  deals that he's worked on over the past year so that you can look at them more deeply.
#  Before you start selecting deals, you'll first figure out what the chances are of 
# selecting certain deals.
#############################################

# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / len(amir_deals['product'])
print(probs)



#############################################
#Sampling deals
#In the previous exercise, you counted the deals Amir worked on. Now it's time to 
# randomly pick five deals so that you can reach out to each customer and ask if they 
# were satisfied with the service they received. You'll try doing this both with and
#  without replacement.Additionally, you want to make sure this is done randomly and 
# that it can be reproduced in case you get asked how you chose the deals, so you'll 
# need to set the random seed before sampling from the deals.
#############################################

np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace=False)
print(sample_without_replacement)

# Set random seed
np.random.seed(24)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace=True)
print(sample_with_replacement)

