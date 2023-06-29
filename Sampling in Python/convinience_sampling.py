########################
#Are findings from the sample generalizable?
#You just saw how convenience sampling—collecting data using the easiest method—can result
# in samples that aren't representative of the population. Equivalently, this means
# findings from the sample are not generalizable to the population. Visualizing the 
#distributions of the population and the sample can help determine whether or not the 
#sample is representative of the population.
#The Spotify dataset contains an acousticness column, which is a confidence measure 
#from zero to one of whether the track was made with instruments that aren't plugged in. 
#You'll compare the acousticness distribution of the total population of songs with a
# sample of those songs.
###################################

# Visualize the distribution of acousticness with a histogram
spotify_population['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
plt.show()

# Update the histogram to use spotify_mysterious_sample
spotify_mysterious_sample['acousticness'].hist(bins=np.arange(0, 1.01, 0.01))
plt.show()


#####################################
#Are these findings generalizable?
#Let's look at another sample to see if it is representative of the population. 
# This time, you'll look at the duration_minutes column of the Spotify dataset, 
# which contains the length of the song in minutes.
##################

# Visualize the distribution of duration_minutes as a histogram
spotify_population['duration_minutes'].hist(bins=np.arange(0,15.5,0.5))
plt.show()

# Update the histogram to use spotify_mysterious_sample2
spotify_mysterious_sample2['duration_minutes'].hist(bins=np.arange(0, 15.5, 0.5))
plt.show()


