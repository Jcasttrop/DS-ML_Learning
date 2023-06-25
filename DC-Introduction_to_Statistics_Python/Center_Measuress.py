import pandas as pd

food_consumption = pd.read_csv('C:\Users\Julian.Castro\Desktop\DS-ML_Learning\DC-Introduction_to_Statistics_Python\food_consumption.csv')

#############################################
#Mean and median
#In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. 
#The food_consumption dataset contains information about the kilograms of food consumed
#per person per year in each country in each food category (consumption) as well as 
# information about the carbon footprint of that food category (co2_emissions) measured in
#  kilograms of carbon dioxide, or CO2, per person per year in each country.
# In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.
#############################################


#Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that
#holds rows for 'USA'. Call these be_consumption and usa_consumption.
# Calculate the mean and median of kilograms of food consumed per person per year for 
# both countries.


# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption.loc[food_consumption['country']=='Belgium']

# Filter for USA
usa_consumption = food_consumption.loc[food_consumption['country']=='USA']

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))


#Subset food_consumption for rows with data about Belgium and the USA.
# Group the subsetted data by country and select only the consumption column.
# Calculate the mean and median of the kilograms of food consumed per person per year
#  in each country using .agg().


# Import numpy as np
import numpy as np

print(food_consumption[food_consumption['country'].isin(['Belgium', 'USA'])])

# Subset for Belgium and USA only
be_and_usa = food_consumption[food_consumption['country'].isin(['Belgium', 'USA'])]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg(['mean', 'median']))


# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt


# Subset for food_category equals rice
rice_consumption = food_consumption.loc[food_consumption['food_category']=='rice']

# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'], bins=10)
plt.show()


