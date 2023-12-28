#!/usr/bin/env python
# coding: utf-8

# #### Write a Python program to create a tuple

# In[2]:


t=(1,2,2.5,'x',)
type(t)


# In[3]:


t[1]


# #### Write a Python program to add an item in a tuple

# In[9]:


t = (10,40,50,70,90)
t=t+(20,)
print(t)
l=list(t)
l.append(30)
t=tuple(l)
t


# #### Write a Python program to convert a tuple to a string
# 
# 
# 

# In[10]:


t = ('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's')
t1=''.join(t)
t1


# #### Write a Python program to get the 4th element and 4th element from last of a tuple

# In[24]:


t = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
a=t[4]
print('4th from start-',a)
b=t[-4]
print('4th from last-',b)


# #### Write a Python program to create the colon of a tuple

# In[26]:


t = ("Tutor", 'J', 23 , 56.67 , [23,12] , True)
t2=
t2


# #### Write a Python program to find the repeated items of a tuple

# In[27]:


t = (2,34,45,6,7,2,4,5,78,34,2)
t.count(2)


# #### Write a Python program to check whether an element exists within a tuple

# In[28]:


t = ('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's',8)
print(8 in t)
print('x' in t)


# #### Write a Python program to convert a list to a tuple

# In[30]:


q=[12, 45, 87, 54, 89, 4]
w=tuple(q)
print(w)
print(type(w))


# #### Write a Python program to remove an item from a tuple

# In[37]:


t2=(23, 45, 56, 68, 10, 45, 7, 9)
print('old tuple-',t2)
l2=list(t2)
l2.remove(56)
t3=tuple(l2)
print('new tuple after removing 56-',t3)


# #### Write a Python program to slice a tuple

# In[46]:


a = (10,20,30,40,50,60,70,80,90,100)
print('from 0 to 5 with step 2-',a[:5:2])
print('from 3 to 8 ',a[3:8])
print('from fistlast to 3rd last-',a[:-3:-1])


# #### Write a Python program to find the index of an item of a tuple

# In[47]:


d=(23, 45, 67, 78, 89, 90, 34, 56)
print('Index of 78-',d.index(78))


# #### Write a Python program to find the length of a tuple
# 

# In[48]:


g=("Lion", "Cat", "Dog", "Panda", "Tiger", "Fox")
len(g)


# #### Write a Python program to convert a tuple to a dictionary
# 

# In[56]:


t4=( ("Name", "Ram"), ("Age", 23), ("City", "Salem"), ("Mark", 422) )
d=(dict((k,v)for k,v in t4))
print(d)
print(type(d))


# #### Write a Python program to unzip a list of tuples into individual lists
# 

# In[59]:


l5=[ (10,30), (60,90), (20,50) ]


# #### Write a Python program to reverse a tuple

# In[61]:


t5=( 23, 45, 67, 78, 89, 90, 34, 56 )
t6=t5[::-1]
print(t6)


# #### Write a Python program to convert a list of tuples into a dictionary

# In[62]:


t7=[ ("Name", "Ram"), ("Name", "Pooja"), ("Age", 21), ("Gender", "Male"), ("Age", 23), ("Gender", 
"Female") ]


# #### Write a Python program to print a tuple with string formatting

# In[64]:


w=("watermelons", "strawberries", "mangoes", "bananas", "grapefruits", "oranges", "apples", 
"pears")
print('fruits{}'.format(w))


# #### Create a tuple with single item 23

# In[67]:


tu1=(23,)
print(type(tu1))


# #### Unpack the tuple into 5 variables
# 

# In[72]:


Tuple = (11, 22, 333, 44, 55)
a,b,c,d,e=Tuple
print(a)
print(b)
print(c)
print(d)
print(e)


# #### Swap two tuples in Python

# In[81]:


ab=(10,)
ba=(20,)
abc=ab
ab=ba
ba=abc
print('after swap ab-',ab)
print('after swap ba-',ba)


# #### Copy specific elements from one tuple to a new tuple
# 

# In[82]:


r=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
r1=r[2:8]
print(r1)


# #### Modify the tuple

# In[86]:


e=( 10, 20, 30, 40, 50 )
print('before modiy tuple -',e)
e1=list(e)
e1[2]=33
e3=tuple(e1)
print('after modify tuple-',e3)


# #### Sort a tuple of tuples by 2nd item

# In[87]:


y=( ('a', 53), ('b', 37), ('c', 23), ('d', 1), ('e', 18) )



# #### Counts the number of occurrences of item 30 from a tuple

# In[88]:


u=(30, 50, 10, 30, 70, 50, 30)
print('count of 30-',u.count(30))


# #### Write a Python program to compute element-wise sum of given tuples
# 

# In[89]:


A = (2, 5, 8)
B = (6, 5, 1)
C = (1, 4, 7)
D = (3, 7, 2)



# #### Write a Python program to sort a tuple by its float elemen

# In[90]:


y=[ ('Ram', '89.20'), ('Siva', '76.45'), ('Pooja', '84.40'), ('Tara', '68.43'), ('Jeeva', '91.40') ]


# #### Write a Python program to replace last value of tuples in a list

# In[91]:


o=[(5, 2, 3), (4, 7, 6), (8, 9, 6)]


# #### Write a Python program to Extract tuples having K digit elements
# 

# In[ ]:





# #### Write a Python program to Extract Symmetric Tuples

# In[92]:


i=[ (18, 23), (2, 9), (7, 6), (9, 2), (10, 2), (23, 18) ]


# #### Write a Python program to Sort Tuples by their Maximum element

# In[93]:


p=[ (4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2) ]


# #### Write a Python program to Concatenate tuples to nested tuples

# In[99]:


Tuple1= ((18, 23, 2, 9),)
Tuple2= ((10, 3, 11),)
tup=(Tuple1 + Tuple2)
print('tuple after concatenating-',tup)


# #### Write a Python program to Sort lists in tuple

# In[101]:


s=( [10, 50, 60], [80, 20, 30], [70, 100, 40], (90,) )
print('tuple before sort-',s)
s1= tuple((sorted(i) for i in s))
print('tuple after sorting-',s1)


# #### Write a Python program to Order Tuples using external List

# In[104]:


x=[ ('B', 68), ('D', 70), ('A', 67), ('C', 69) ]
x1=['A','B','C','D']
x2=dict(x)
x3=[(key,x2[key]) for key in x1]
print('ordered tuple-',x3)


# In[ ]:





# In[106]:


s= [(3, 4), (1, 2), (4, 3), (5, 6)]
l=list(set(tuple(sorted(s))))
count=len(l)
print('unique tuple frequency-',l)
print('unique tuple frequency count-',count)


# #### Write a Python program to Tuple XOR operation

# In[112]:


t1 = (10, 4, 6, 9)
t2 = (5, 2, 3, 3)
res = tuple(e1 ^ e2 for e1, e2 in zip(t1, t2))
print("The XOR tuple : " + str(res))
 


# In[ ]:





# In[ ]:





# In[ ]:




