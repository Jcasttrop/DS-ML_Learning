world_happiness = pd.read_csv('world_happiness.csv')

#############
#Relationships between variables
#The report scores various countries based on how happy people in that country are. 
# It also ranks each country on various societal aspects such as social support, freedom,
#  corruption, and others. The dataset also includes the GDP per capita and life 
# expectancy for each country.
#############

# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x='life_exp',y='happiness_score', data=world_happiness)
# Show plot
plt.show()

# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp',y='happiness_score', data=world_happiness, ci=None)
# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['happiness_score'].corr(world_happiness['life_exp'])

print(cor)


###############
#What can't correlation measure?
#While the correlation coefficient is a convenient way to quantify the strength of a 
# relationship between two variables, it's far from perfect. In this exercise, you'll 
# explore one of the caveats of the correlation coefficient by examining the relationship
#  between a country's GDP per capita (gdp_per_cap) and happiness score.
###############

# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap',y='life_exp', data=world_happiness)

# Show plot
plt.show()

#Este ejercicio se trato sobre la correlacion no lineal


###############
#Transforming variables
#When variables have skewed distributions, they often require a transformation in order 
# to form a linear relationship with another variable so that correlation can be computed. 
# In this exercise, you'll perform a transformation yourself.
###############

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='happiness_score',y='gdp_per_cap', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['gdp_per_cap'])
print(cor)


# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='happiness_score',y='log_gdp_per_cap', data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness['happiness_score'].corr(world_happiness['log_gdp_per_cap'])
print(cor)

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day',y='happiness_score', data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)


###############
#Does sugar improve happiness?
#A new column has been added to world_happiness called grams_sugar_per_day,
#  which contains the average amount of sugar eaten per person per day in each country.
#  In this exercise, you'll examine the effect of a country's average sugar consumption on 
# its happiness score.
###############

# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x='grams_sugar_per_day',y='happiness_score', data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])
print(cor)





