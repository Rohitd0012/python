#!/usr/bin/env python
# coding: utf-8

# #### Write a Python program to sum all the items

# In[8]:


A=[1,7,-10,34,2,-8]
print(sum(A))


# #### Write a Python program to multiply all the items in a list

# In[1]:


b=[3,4,5,4,7]
print((b))


# #### Write a Python program to get the largest number from a list

# In[10]:


c=[1,7,10,34,2,8]
print(max(c))


# #### Write a Python program to get the smallest number from a list
# 

# In[11]:


d=[51,7,10,34,2,8]
print(min(d))


# #### Write a Python program to count the number of strings

# In[13]:


e=['abc', 'xyz', 'aba', '1221']
print(len(e))


# #### Write a Python program to remove duplicates from a list
# 

# In[7]:


f=[1,2,3,7,2,1,5,6,4,8,5,4]
print(list(set(f)))


# #### Write a Python program to check a list is empty or not

# In[9]:


g=[34,45,6,5,4,56,7]
if (len(g))==0:
    print('list is empty')
else :
    print('list is not empty')


# #### Write a Python program to clone or copy a list

# In[16]:


#using copy 
h=[10, 22, 44, 23, 4]
h1=h.copy()
h1


# In[15]:


#by using assign
h=[10, 22, 44, 23, 4]
h2=h
h2


# #### '''Write a Python program to find the list of words that are longer than n from a given list 
# of word'''

# In[21]:


i=['Words', 'Longer', 'given', 'Words','tftfrdsr','dses0','ffdses','fdssgtf','okju','jh','w']
n=4
for x in i:
      if len(x)>n:
        print(x)


# #### Write a Program that get two lists as input and check if they have at least one common 
# member

# In[1]:


j=[1,2,3,4,5]
k=[5,6,7,8,9]


# #### Write a Python program to print a specified list after removing the 0th, 4th and 5th 
# elements. (enumerate)

# In[3]:


l=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
l()


# #### Write a Python program to print the numbers of a specified list after removing even 
# numbers from it
# 

# In[4]:


m=[7,32,81,20,25,14,23,27]


# #### Write a Python program to shuffle and print a specified list (shuffle

# In[7]:


n=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
from random import shuffle
shuffle(n)
print(n)


# #### Write a Python program to generate and print a list of first and last 5 elements where 
# the values are square of numbers between 1 and 30
# 
# 
# 
# 
# 

# In[14]:


o=[]
for i in range (1,31):
    o.append(i*i)
print(o[:5])
print(o[-5:])


# #### Write a Python program to generate all permutations of a list in Python. (itertools

# In[15]:


p=[1,2,3]



# #### Write a Python program to convert a list of characters into a string
# 

# In[16]:


q=['T','u','t','o','r',' ','J','o','e','s']
q1=''.join(q)
q1


# #### Write a Python program to find the index of an item in a specified list

# In[23]:


s=[20, 70, 30, 90, 10, 30, 90, 10, 80]
print(s.index(30))
print(s[4])


# #### Write a Python program to flatten a shallow lis

# In[24]:


r=[[20,30,70],[30,90,10], [30,20], [70,90,10,80]]


# #### Write a Python program to add a list to the second list

# In[26]:


t=[10, 20, 30, 40]
t1=["Cat", "Dog", "Lion", "Ponda"]
t2=t+t1
t2


# #### Write a Python program to select an item randomly from a list Using random.choice()

# In[29]:


u=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
import random
random.choice(u)


# #### Write a python program to check whether two lists are circularly identical
# 

# In[30]:


a1=[8, 8, 12, 12, 8]
a2=[8, 8, 8, 12, 12]
a3=[1, 8, 8, 12, 12]


# #### Write a Python program to find the second smallest number in a list

# In[31]:


b2=[2,4,56,78,4,34,5,8,9]



# #### Write a Python program to find the second largest number in a list

# In[32]:


[82,4,56,78,4,34,5,100,9]


# #### Write a Python program to get unique values from a list

# In[33]:


c1=[82, 4, 10, 56, 78, 4, 34, 5, 10, 9]


# #### Write a Python program to get the frequency of the elements in a list.

# In[34]:


d1=[10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]


# #### Create a list by concatenating a given list which range goes from 1 to n

# In[35]:


e1=['T', 'J']


# #### Write a Python program to find common items from two lists

# In[36]:


n1 = [23,45,67,78,89,34]
n2 = [34,89,55,56,39,67]
print(set(n1) & set(n2))
 


# #### Write a Python program to split a list based on first character of word
# 

# In[ ]:





# #### Write a Python Program to Swap elements in String list
# 

# In[38]:


l1=['Tutor', 'joes', 'Computer', 'Education']


# #### Write a Python program to reverse All Strings in String List

# In[40]:


s1= ["Tutor","joes","Computer","Education"]
s2=s1[::-1]
s2


# In[ ]:




