#!/usr/bin/env python
# coding: utf-8

# # Stats: Simulation

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Each of the following problems will require these steps:
#1. Represent data
#2. Make a matrix
#3. Aggregate


# # Problem 1

# In[3]:


#1. How likely is it that you roll doubles when rolling two dice?


# In[4]:


n_trials = n_cols = 2
n_sims = n_rows = 100_000

dice_rolls = pd.DataFrame(np.random.choice([1, 2, 3, 4, 5, 6], size=(n_sims, n_trials)))
dice_rolls


# In[5]:


roll_doubles = dice_rolls[0] == dice_rolls[1]
roll_doubles


# In[6]:


probability_of_doubles = roll_doubles.mean()
probability_of_doubles


# # Problem 2

# In[7]:


#2. If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?


# In[8]:


n_trials = 8
n_sims = 100_000

# 1 is  heads, 0 is tails
coin_flips = np.random.choice([0, 1], size=(n_sims, n_trials))
coin_flips


# In[9]:


exactly_3_heads = (coin_flips == 1).sum(axis=1) == 3
exactly_3_heads.mean()


# In[10]:


more_than_3_heads = (coin_flips == 1).sum(axis=1) > 3
more_than_3_heads


# In[11]:


more_than_3_heads.mean()


# # Problem 3

# In[12]:


#3. There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?


# In[13]:


n_trials = 2
n_sims = 100_000

billboards = np.random.choice(['Web Dev', 'Data Science'], p=[.75, .25], size=(n_sims, n_trials))
billboards


# In[14]:


df = pd.DataFrame(billboards)
df.columns = ["first_billboard", "second_billboard"]
df.head()


# In[15]:


df["both_ds"] = (df.first_billboard == "Data Science") & (df.second_billboard == "Data Science")
df["both_ds"].mean()


# # Problem 4

# In[16]:


#4. Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?


# In[17]:


n_trials = ncols = 5
n_sims = nrows = 100_000

poptart_purchases = np.random.normal(3,1.5, size = (n_sims, n_trials))
rounded_poptart_purchases = poptart_purchases.round()
rounded_poptart_purchases


# In[18]:


no_neg_poptarts = np.where(rounded_poptart_purchases < 0, 0, rounded_poptart_purchases)
no_neg_poptarts


# In[19]:


poptarts_on_friday = no_neg_poptarts.sum(axis=1) < 17
poptarts_on_friday.mean()


# # Problem 5

# In[20]:


#5. Compare Heights


# In[21]:


# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?


# In[22]:


men_height = np.random.normal(178, 8, size = 100_000)
men_height


# In[23]:


women_height = np.random.normal(170, 6, size = 100_000)
women_height


# In[24]:


height = pd.DataFrame({'Average Mens Height': men_height, 'Average Womens Height': women_height})
height


# In[25]:


height['Woman is taller than Man'] = (height['Average Womens Height'] > height['Average Mens Height'])
height


# In[26]:


probability_woman_is_taller_than_man= height['Woman is taller than Man'].mean()
probability_woman_is_taller_than_man


# # Problem 6

# In[27]:


#6. When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?


# In[28]:


def prob_no_anaconda_corruption(students, number_of_sims_to_run):
    n_trials = n_cols = students
    n_sims = n_rows = number_of_sims_to_run

    installs = np.random.choice([0, 1], p=[1/250, 249/250], size=(n_rows, n_cols))
    
    no_corruptions = installs.sum(axis=1) == students
    
    return no_corruptions.mean()


# In[29]:


prob_no_anaconda_corruption(50, 100_000)


# In[30]:


#for 100 students?


# In[31]:


prob_no_anaconda_corruption(100, 100_000)


# In[32]:


# What is the probability that we observe an installation issue within the first 150 students that download anaconda?


# In[33]:


def prob_anaconda_corruption(students, number_of_sims_to_run):
    n_trials = n_cols = students
    n_sims = n_rows = number_of_sims_to_run

    installs = np.random.choice([0, 1], p=[1/250, 249/250], size=(n_rows, n_cols))
    
    has_corruptions = installs.sum(axis=1) < students
    
    return has_corruptions.mean()


# In[34]:


prob_anaconda_corruption(150, 100_000)


# In[35]:


# How likely is it that 450 students all download anaconda without an issue?


# In[36]:


prob_anaconda_corruption(450, 100_000)
(249/250)**450


# # Problem 7

# In[37]:


#7. There's a 70% chance on any given day that there will be at least one food truck at Travis Park. However, you haven't seen a food truck there in 3 days. How unlikely is this?


# In[38]:


n_trials = 3
n_sims = 100_000

# 0 is no food trucks, 1 is at least 1 food truck
food_trucks = np.random.choice([0, 1], p=[.3, .7], size=(n_sims, n_trials))
food_trucks


# In[39]:


no_food_trucks = food_trucks.sum(axis=1) == 0
no_food_trucks


# In[40]:


no_food_trucks.mean()


# In[41]:


# How likely is it that a food truck will show up sometime this week?


# In[42]:


n_trials = 7
n_sims = 100_000

food_trucks = np.random.choice([0, 1], p=[.3, .7], size =(n_sims, n_trials))
food_trucks


# In[43]:


at_least_one_food_truck = food_trucks.sum(axis=1) > 0
at_least_one_food_truck


# In[44]:


at_least_one_food_truck.mean()


# # Problem 8

# In[45]:


#8. If 23 people are in the same room, what are the odds that two of them share a birthday? What if it's 20 people? 40?


# In[ ]:


birthdays = np.random.randint(1,365, (100_000, 23))
birthdays_df = pd.DataFrame(birthdays)
(birthdays_df.nunique(axis=1) < 23).mean()


# In[ ]:


birthdays = np.random.randint(1,365, (100_000, 20))
birthdays_df = pd.DataFrame(birthdays)
(birthdays_df.nunique(axis=1) < 20).mean()


# In[ ]:


birthdays = np.random.randint(1,365, (100_000, 40))
birthdays_df = pd.DataFrame(birthdays)
(birthdays_df.nunique(axis=1) < 40).mean()

