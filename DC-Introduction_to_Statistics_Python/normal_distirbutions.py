import pandas as pd
from scipy.stats import norm

amir_deals = pd.read_csv('amir_deals.csv')

# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()

print(np.mean(amir_deals['amount'])) #4812.000337078652
print(np.std(amir_deals['amount'])) #2052.3836970784955

#The amir_deals data ollow a normal distribution with a mean of 4812 and a standard deviation of 2052.

#What's the probability of Amir closing a deal worth less than $7500?
prob_less_7500 = norm.cdf(7500, 5000, 2000)

# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

#What's the probability of Amir closing a deal worth between $3000 and $7000?
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)


##################
#Simulating sales under new market conditions
#The company's financial analyst is predicting that next quarter, 
# the worth of each sale will increase by 20% and the volatility, or standard deviation,
#  of each sale's worth will increase by 30%. To see what Amir's sales might look
#  like next quarter under these new market conditions, you'll simulate new sales
#  amounts using the normal distribution and store these in the new_sales DataFrame, 
# hich has already been created for you.
#####################

#Currently, Amir's average sale amount is $5000. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.
new_mean = 5000 + (5000*0.20) #Is equal to 5000 * 1.20

#Amir's current standard deviation is $2000. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.
new_sd = 2000 + (2000*0.30) 

#Create a variable called new_sales, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of new_sd.
new_sales = norm.rvs(new_mean, new_sd, size=36)

# Create histogram and show
plt.hist(new_sales)
plt.show()

#Which market is better?
#The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.
#Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.

norm.cdf(1000, 5000, 2000)
norm.cdf(1000, 6000, 2600)