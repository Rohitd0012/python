#!/usr/bin/env python
# coding: utf-8

# # EDA on Airbnb NYC 2019
# ### BY ROHIT 
# 
# Airbnb is an online marketplace that connects people who want to rent out their homes with people looking for accommodations in that locale. NYC is the most populous city in the United States, and one of the most popular tourism and business places globally.
# Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present a more unique, personalized way of experiencing the world. Nowadays, Airbnb became one of a kind service that is used by the whole world. Data analysts become a crucial factor for the company that provided millions of listings through Airbnb. These listings generate a lot of data that can be analyzed and used for security, business decisions, understanding of customers’ and providers’ behavior on the platform, implementing innovative additional services, guiding marketing initiatives, and much more.
# 
# Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present a more unique, personalized way of experiencing the world. Today, Airbnb became one of a kind service that is used and recognized by the whole world. Data analysis on millions of listings provided through Airbnb is a crucial factor for the company. These millions of listings generate a lot of data - data that can be analyzed and used for security, business decisions, understanding of customers' and providers' (hosts) behavior and performance on the platform, guiding marketing initiatives, implementation of innovative additional services and much more.
# This dataset has around 49,000 observations in it with 16 columns and it is a mix between categorical and numeric values.
# 
# ## GitHub Link
# https://github.com/Rohitd0012/python/tree/main/AIRBNB
# 

# ### Importing important packages

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# ### Loading the dataset

# In[3]:


data = pd.read_csv('https://raw.githubusercontent.com/Rohitd0012/python/main/AIRBNB/Airbnb%20NYC%202019.csv')
data.head()


# ### Data Description
# **Id** : Unique for each Propety Listing. <br>
# **name** : Name of the each Propety Listing. <br>
# **host_id** : Unique ID for host who have listed the property on Airbnb. <br>
# **host_name** : Name of host <br>
# **neighbourhood_group** : Name of Each boroughs of NYC, Manhattan, Brooklyn,Queens,Bronx, State Island. <br>
# **neighbourhood** : Area in each borough of NYC <br>
# **latitude, longitude** : Co-ordinates of each listed property <br>
# **room_type** : Differnt types of room available for listing , Private room,Entire home/apt,Shared room. <br>
# **price** : Price of listing. <br>
# **minimum_nigths** : Mandatory number of nights to be booked for available for each type of property. <br>
# **number_of_review** : Number of reviews for each Listed property <br>
# **last_review** : Date on whcih last time the listing was reviewed <br>
# **review_per_month** : Number of reviews per month <br>
# **calculated_host_listings_count** : Number of listing each host owns <br>
# **availablity_365** : Number of days the given listing is available for booking <br>

# In[4]:


# Copying the data
df = data.copy()


# In[6]:


# Getting the info
df.info()


# ### What is Describe ?
# **The describe() method returns description of the data in the DataFrame. If the DataFrame contains numerical data, the description contains these information for each column: count - The number of not-empty values. mean - The average (mean) value. std - The standard deviation.**

# ### FInding the duplicated values

# In[7]:


df.describe().T.style.background_gradient()


# In[8]:


df.duplicated().sum()


# ### There are no duplicated values

# In[9]:


df.shape


# In[10]:


df.head()


# In[11]:


df.isnull().sum()


# ### Replacing the null values with appropriate values

# In[12]:


df['name'].replace(np.nan, 'Other Hotel', inplace =True)
df['host_name'].replace(np.nan, 'other', inplace = True)
df['last_review'].replace(np.nan, 'Not Reviewed', inplace = True)
df['reviews_per_month'].replace(np.nan, '0', inplace = True)


# In[13]:


df.info()


# ### We dont need id and last_reviewed as it is completely unique and has no significance for visualization

# In[14]:


df.drop(['id', 'last_review'], axis = 1, inplace = True)


# ### Also dropping the name column as it signifies nothing.

# In[15]:


df.drop(['name'], axis = 1, inplace = True)


# In[16]:


df.isnull().sum()


# ### Hence the data is free from duplicates and null values and is ready for visualization.

# ## Data Visualization

# ### 1. Top 10 Host name

# In[17]:


df.head()


# In[18]:


# Getting the value counts
df['host_name'].value_counts().iloc[:10]


# In[19]:


# Visualizing using bar plot
plt.figure(figsize = (15,6))
sns.barplot(data = df, x = df['host_name'].value_counts().iloc[:10].keys(), 
           y = df['host_name'].value_counts().iloc[:10])
plt.title("Top Host name performer", fontsize = 15)
plt.show()


# ### Observation
# 1. Host name is the name of the host who listed the hotel in the airbnb.
# 2. It looks like the persom Michael has the lasrgest booking under his name with 417 bookings
# 3. David is the host name with 403 bookings.

# ### 2. Neighbourhood_group.
# #### Neighbourhood_group - Name of Each boroughs of NYC, Manhattan, Brooklyn,Queens,Bronx, State Island

# In[20]:


df.head()


# In[21]:


# Getting the vlaue count
df['neighbourhood_group'].value_counts()


# In[22]:


# Visualizing using pie chart
df['neighbourhood_group'].value_counts().plot(kind = 'pie', figsize = (8,8), autopct = '%1.1f%%', fontsize = 15)
plt.title("Neighbourhood Group", fontsize = 25)
plt.show()


# ### Observation
# 1. **neighbourhood_group** : Name of Each boroughs of NYC, Manhattan, Brooklyn,Queens,Bronx, State Island.
# 2. It looks like Manhatten group has the largest bookings
# 3. Followed by brooklyn with 41.1% share.

# ### 4. Finding the top 10 host_id
# #### Host_id - Unique ID for host who have listed the property on Airbnb.

# In[23]:


df.head()


# In[24]:


# Finding the value count
df['host_id'].value_counts().reset_index().iloc[:10]


# In[25]:


# Plotting the bar graph for that
plt.figure(figsize = (13,6))
sns.barplot(x=df['host_id'].value_counts().iloc[:10].keys(), y=df['host_id'].value_counts().iloc[:10], data=df,
                 palette='bright')
plt.title("Hosts with the most listings in NYC", fontsize = 15)
plt.xlabel("Host IDs", fontsize = 15)
plt.ylabel("Count of listings", fontsize = 15)
plt.show()


# ### Observation
# 1. We can see that there is a good distribution between top 10 hosts with the most listings.
# 2. First host has more than 300+ listings.

# ### 5. Neighbourhood_group according to price

# In[26]:


df.head()


# In[27]:


df.shape


# In[28]:


plt.figure(figsize = (15,6))
sns.boxplot(x = df['price'])
plt.show()


# ### Boxplot - 
# A box plot is a chart that shows data from a five-number summary including one of the measures of central tendency. It does not show the distribution in particular as much as a stem and leaf plot or histogram does. But it is primarily used to indicate a distribution is skewed or not and if there are potential unusual observations (also called outliers) present in the data set. Boxplots are also very beneficial when large numbers of data sets are involved or compared.

# ![box.png](attachment:box.png)

# In[29]:


# Getting the mathematical answers for the price column
df['price'].describe()


# ## Probability density Function graph 
# A function that defines the relationship between a random variable and its probability, such that you can find the probability of the variable using the function, is called a Probability Density Function (PDF) in statistics.

# In[30]:


plt.figure(figsize = (15,6))
sns.distplot(df['price'], color = 'red', hist_kws={"linewidth": 15,'alpha':1})
plt.title("Probability Distribution", fontsize = 15)
plt.xlabel('Price', fontsize = 15)
plt.ylabel('Density', fontsize = 15)
plt.show()


# ### Normal Distribution
# A normal distribution is a type of continuous probability distribution in which most data points cluster toward the middle of the range, while the rest taper off symmetrically toward either extreme. The middle of the range is also known as the mean of the distribution.

# ![PDG-2.jpg](attachment:PDG-2.jpg)

# ### Calculating the interquartile ranges

# In[31]:


Q1 = np.percentile(data['price'], 25, interpolation = 'midpoint')
  
# Third quartile (Q3)
Q3 = np.percentile(data['price'], 75, interpolation = 'midpoint')
  
# Interquaritle range (IQR)
IQR = Q3 - Q1

print('The IQR is',IQR)
print('The Minimum value is', (Q3 - (1.5* (IQR))))
print('The maximum value is', (Q3 + (1.5* (IQR))))


# ### As we can see that 99% of the data lies withing 334 dollar with mean being 153 and median 106.

# In[32]:


df_new = df[df['price'] < 334 ]
df_new.head()


# In[33]:


df.groupby(['neighbourhood_group'])['price'].describe().T.reset_index()


# In[34]:


df_new.groupby(['neighbourhood_group'])['price'].describe().T.reset_index()


# In[35]:


plt.figure(figsize = (15,6))
sns.violinplot(data = df_new, x = df_new['neighbourhood_group'], y = df_new['price'])
plt.title('Density and distribution of prices for each neighberhood_group', fontsize = 15)
plt.grid()


# ### Violin Plot
# A violin plot is a hybrid of a box plot and a kernel density plot, which shows peaks in the data. It is used to visualize the distribution of numerical data. Unlike a box plot that can only show summary statistics, violin plots depict summary statistics and the density of each variable.
# 

# In[36]:


plt.figure(figsize = (16,15))

plt.subplot(3,2,1)
n1 = df_new[df_new['neighbourhood_group'] == 'Brooklyn']
sns.distplot(x = n1['price'])
plt.title("Brooklyn", fontsize = 15)

plt.subplot(3,2,2)
n2 = df_new[df_new['neighbourhood_group'] == 'Manhattan']
sns.distplot(x = n2['price'])
plt.title("Manhattan", fontsize = 15)

plt.subplot(3,2,3)
n3 = df_new[df_new['neighbourhood_group'] == 'Queens']
sns.distplot(x = n3['price'])
plt.title("Queens", fontsize = 15)

plt.subplot(3,2,4)
n4 = df_new[df_new['neighbourhood_group'] == 'Staten Island']
sns.distplot(x = n4['price'])
plt.title("Staten Island", fontsize = 15)

plt.subplot(3,2,5)
n5 = df_new[df_new['neighbourhood_group'] == 'Bronx']
sns.distplot(x = n5['price'])
plt.title("Bronx", fontsize = 15)


# ### Histplot
# Histplot is a combination of 3 plots. <br>
# **1. Histogram** - A histogram is a bar graph-like representation of data that buckets a range of classes into columns along the horizontal x-axis. The vertical y-axis represents the number count or percentage of occurrences in the data for each column. Columns can be used to visualize patterns of data distributions. <br>
# 
# **2. KDE** - Kernal Density Estimation - Kdeplot is a Kernel Distribution Estimation Plot which depicts the probability density function of the continuous or non-parametric data variables i.e. we can plot for the univariate or multiple variables altogether. <br>
# 
# **3. Rugplot** - A rug plot is a plot of data for a single quantitative variable, displayed as marks along an axis. It is used to visualise the distribution of the data. As such it is analogous to a histogram with zero-width bins, or a one-dimensional scatter plot.

# In[37]:


plt.figure(figsize = (10,6))
sns.distplot(x = n5['price'],  rug = True, color ='r')
plt.title(" Histplot for Bronx containing Histogram, KDE and Rugplot", fontsize = 15)
plt.show()


# ### Observation
# 1. we can observe that state that Manhattan has the highest range of prices for the listings with 150 price as median observation, followed by Brooklyn with 90 per night.
# 2. Queens and Staten Island appear to have very similar distributions, Bronx is the cheapest of them all. 
# 3. This distribution and density of prices were completely expected; for example, as it is no secret that Manhattan is one of the most expensive places in the world to live in, where Bronx on other hand appears to have lower standards of living.

# ### 6. Room type

# In[38]:


df.head()


# In[39]:


# Getting the value counts
df['room_type'].value_counts()


# In[40]:


# Visualizing using pie chart
df['room_type'].value_counts().plot(kind = 'pie', figsize = (8,8), fontsize = 15, autopct = '%1.1f%%')
plt.title("Room Types", fontsize = 15)


# ### Observation
# 1. Most of the people happen to rent the entire home or apartment which constitutes to 52% according to the chart.
# 2. Followed by 45.7% people consider having private room, and shared is the least considered room type.

# ### 7. Prices for different room type

# In[41]:


df.head()


# In[42]:


df.groupby(['room_type'])['price'].mean().reset_index()


# In[43]:


df.groupby(['room_type'])['price'].mean().plot(kind = 'bar', figsize = (10,6), color = 'g')
plt.xticks( rotation = 360)
plt.title("Average price of different room types", fontsize = 15)
plt.xlabel('Room_Types', fontsize = 15)
plt.ylabel('mean', fontsize = 15)
plt.show()


# In[44]:


df.groupby(['room_type'])['price'].describe()


# In[45]:


plt.figure(figsize = (16,10))

plt.subplot(1,3,1)
entire = df[df['room_type'] == 'Entire home/apt']
plt.boxplot(x  = entire['price'])
plt.title("Entire home/apt", fontsize = 15)

plt.subplot(1,3,2)
private = df[df['room_type'] == 'Private room']
plt.boxplot(x  = private['price'])
plt.title("Private room", fontsize = 15)

plt.subplot(1,3,3)
shared = df[df['room_type'] == 'Shared room']
plt.boxplot(x  = shared['price'])
plt.title("Shared room", fontsize = 15)

plt.show()


# ### Observation
# 1. As we can see from the boxplot, the room type Entire home/apt has highest price going upto 10000 dollars, also it has a lot of outliers which means that the average price would be higher compared to the other two.
# 2. On the other hand, Private room has less outliers compared to the entire home/apt but the price also goes upto 10000 dollars. But, it has the avergae price of 90 dollar approximately.
# 3. Shared room is the least preffered room type and it also reflect to the the mean price and outliers. The maximum price of the shared room is only 1000 dollars and has the average price revolving around 70 dollar.

# ### 8. Minimum nights for different room types

# In[46]:


df.head()


# In[47]:


# getting the average of the minimum night and rounding it off to 0.
round(df.groupby(['room_type'])['minimum_nights'].mean().reset_index(), 0)


# In[48]:


# Visualizing wrt bar graph
round(df.groupby(['room_type'])['minimum_nights'].mean(), 0).plot(kind = 'bar', figsize = (10,6), fontsize = 10)
plt.xticks(rotation = 360)
plt.title("Minimum average stay", fontsize = 15)
plt.xlabel("Room Type", fontsize = 15)
plt.ylabel("Mean Days", fontsize = 15)
plt.show()


# ### Drawing the Boxplot so that we can has an idea about extreme values

# In[49]:


plt.figure(figsize = (16,10))

plt.subplot(1,3,1)
entire1 = df[df['room_type'] == 'Entire home/apt']
plt.boxplot(x  = entire1['minimum_nights'])
plt.title("Entire home/apt", fontsize = 15)

plt.subplot(1,3,2)
private1 = df[df['room_type'] == 'Private room']
plt.boxplot(x  = private1['minimum_nights'])
plt.title("Private room", fontsize = 15)

plt.subplot(1,3,3)
shared1 = df[df['room_type'] == 'Shared room']
plt.boxplot(x  = shared1['minimum_nights'])
plt.title("Shared room", fontsize = 15)

plt.show()


# ### Observation
# #### If outliers are taken into consideration, then
# 1. According to the data, he mimimum days to stays in entire home/apt is 9 days, also it has maximum price.
# 2. The minimum days to stay for private room 5 days.
# 3. The minimum days to stay for shared room is 6 days.

# ### 9. Avaibility 365

# In[50]:


df.head()


# In[51]:


df['availability_365'].value_counts().iloc[:10].sort_index()


# In[58]:


df['availability_365'].value_counts().iloc[:10].sort_index().plot(kind = 'bar', figsize = (12,6), color = 'm', fontsize = 10)
plt.xticks(rotation = 360)
plt.title('Availability 365', fontsize = 15)


# ### 10. Neighbouthood group with respect to room type

# In[59]:


df.head()


# In[61]:


plt.figure(figsize = (13,8))
sns.countplot(df.neighbourhood_group, hue=df.room_type, palette="bright")
plt.title("Room Type on Neighbourhood Group", fontsize = 15)
plt.show()


# ### Observation
# 1. It looks like, the neighbourhood group Manhatten has the highest Entire home amongst all othergroups.
# 2. but Brooklyn has the most number iof private rooms.
# 3. Manhatten and Brooklyn has almost same number of Shared room.

# ### 11. finding the top 10 and bottom 10 of the neighbourhood

# In[ ]:


df.head()


# In[ ]:


print(df['neighbourhood'].value_counts().iloc[:10], '\n')
print(df['neighbourhood'].value_counts().tail(10))


# In[62]:


plt.figure(figsize = (17,8))

plt.subplot(1,2,1)
sns.barplot(data = df, y = df['neighbourhood'].value_counts().iloc[:10].keys(), 
            x = df['neighbourhood'].value_counts().iloc[:10])
plt.title("Top 10 Neighbourhood", fontsize = 15)

plt.subplot(1,2,2)
sns.barplot(data = df, y = df['neighbourhood'].value_counts().tail(10).keys(), 
            x = df['neighbourhood'].value_counts().tail(10)).invert_xaxis()
plt.title("Bottom 10 Neighbourhood", fontsize = 15)


# ### Observation
# 1. Williamsburg and Bedford - Stuyvesant are the two highest Neighbourhood
# 2. willowbrook, Rossville, New Dorp, Richmondtown and woodrow are the least of the neighbourhood.

# ### Conclusion
# This Airbnb ('AB_NYC_2019') dataset for the 2019 year appeared to be a very rich dataset with a variety of columns that allowed us to dive deep into each significant column presented.
# 
# To begin, firstly, we identified the data of top ten host_id and we figured out that top host ID has 327 listings.
# 
# Secondly, we take "Neighbourhood_Group", and we found that Airbnb listings in New York City are concentrated in five neighborhoods: "Brooklyn," "Manhattan," "Queens," "Staten Island," and "Bronx". Moreover, we also learned from this chart that "Manhattan" and "Brooklyn" have the most hotel properties. Then, we found that Manhattan is the most expensive as the rental charges are more evenly distributed across all the price ranges, median price in Manhattan is approx $150 thats around double the median price of Bronx and the distributions in Queens and Staten Island appear to be very similar, while the Bronx appears to be the cheapest of the three.
# 
# Thirdly, we take the data of "room_type" and figured out that it is devided into three subcategaries and we can observe that the Entire Home/Apartment has the highest share, followed by the Private Room, and the least preferred is Shared Room. Futhermore, entire Home/Apartment is listed most near Manhattan, while Private Rooms and Apartments Near Brooklyn are Nearly equal.
# 
# Fourthly, we put our latitude and longitude columns to good use by creating a geographical map of Newyork city which represents the location of all the areas with their latitude and longtitude. In other map is Color-coded for listing price of room as per the location.
# 
# In addition, we returned to the first column "name" and found out the words from the hotel names, as well as the count for the most frequently used words by hosts. Hosts prefer to use Private rooms,brooklyn,central park,modern,nyc and Beautiful these words in their listing to seek customer attention.
# 
# Finally, we looked for the listings with the "most reviews". Count the rating of top ten reviewed hotels, and found out The top 10 most reviewed listings on Airbnb for NYC have an average price of $65 per night, with the majority of them under 50, and 9/10 of them are "Private Room" types, with the top reviewed listing having 629 reviews.

# In[ ]:





# In[ ]:





# In[ ]:




