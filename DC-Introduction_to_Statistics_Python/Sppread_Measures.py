#############################################
#Quantiles are a great way of summarizing numerical data since they can be used to
#  measure center and spread, as well as to get a sense of where a data point stands in
#  relation to the rest of the data set. For example, you might want to give a discount to 
# the 10% most active users on a website.
# In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a
#  dataset into 4, 5, and 10 pieces, respectively.
#############################################


# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1,5)))

# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1,6)))

# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0,1,11)))


#############################################|
#Variance and standard deviation are two of the most common ways to measure the spread 
# of a variable, and you'll practice calculating these in this exercise. Spread is 
# important since it can help inform expectations. For example, if a salesperson sells a 
# mean of 20 products a day, but has a standard deviation of 10 products, there will 
# probably be days where they sell 40 products, but also days where they only sell one 
# or two. Information like this is important, especially when making predictions.
#############################################

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# copy_f = food_consumption.copy()
# beef = copy_f[copy_f['food_category']=='beef']
# eggs = copy_f[copy_f['food_category']=='eggs']

# Create histogram of co2_emission for food_category 'beef')
plt.hist(food_consumption[food_consumption['food_category']=='eggs']['co2_emission'], bins=10)
# Show plot
plt.show()


# Create histogram of co2_emission for food_category 'eggs'
plt.hist(food_consumption[food_consumption['food_category']=='eggs']['co2_emission'], bins=10)
# Show plot
plt.show()



#############################################
#Outliers can have big effects on statistics like mean, as well as statistics that rely
#  on the mean, such as variance and standard deviation. Interquartile range, or IQR, is 
# another way of measuring spread that's less influenced by outliers. IQR is also often 
# used to find outliers. If a value is less than or greater than 
# it's considered an outlier. In fact, this is how the lengths of the whiskers in 
# a matplotlib box plot are calculated.
#############################################




# Calculate total co2_emission per country: emissions_by_country
emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

# Compute the first and third quantiles and IQR of emissions_by_country
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)