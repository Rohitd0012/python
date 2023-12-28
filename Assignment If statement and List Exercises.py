#!/usr/bin/env python
# coding: utf-8

# ###### Write a program that reads an integer from the user. Then yourprogram should display a message indicating whether the integer is even or odd.
# 

# In[5]:


A=int(input('Enter integer-'))
if A%2 == 0:
    print('interger is even')
else:
    print('integer is odd')


# ###### Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years. Your program should display an appropriate error message if the user enters a negative number.

# ###### Create a program that reads a letter of the alphabet from the user. If the user enters a, e, i, o or u then your program should display a message indicating that the entered letter is a vowel. If the user enters y then your program should display a message indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your program should display a message indicating that the letter is a consonant.

# In[7]:


vowels=['a','e','i','o','u']
letter=str(input('Enter a letter of the alphabet-'))
if letter in vowels:
    print('letter is vowel')
elif letter == 'y' or 'Y':
    print('sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('letter is constant')


# ###### Write a program that determines the name of a shape from its number of sides. Read the number of sides from the user and then report the appropriate name as part of a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of this range is entered then your program should display an appropriate error message

# In[17]:


sides=int(input('Enter number of sides-'))

if sides==3:
    print('number of sides are',sides,', so name of shape is Triangle')
elif sides ==4:
    print('number of sides are',sides,', so name of shape is Square')
elif sides ==5:
    print('number of sides are',sides,', so name of shape is Pentagon')
elif sides ==6:
    print('number of sides are',sides,', so name of shape is Hexagon')
elif sides ==7:
    print('number of sides are',sides,', so name of shape is Heptagon')
elif sides ==8:
    print('number of sides are',sides,', so name of shape is Octagon')
elif sides ==9:
    print('number of sides are',sides,', so name of shape is Nonagon')
elif sides == 10:
    print('number of sides are',sides,', so name of shape is Decagon')
else:
    print('out of range, please enter sides between range 3 to 10')


# ###### The length of a month varies from 28 to 31 days. In this exercise you will create a program that reads the name of a month from the user as a string. Then your program should display the number of days in that month. Display “28 or 29 days” for February so that leap years are addressed.

# In[21]:


A30=['april','june','september','november']
A31=['january','march','may','july','august','octomber','december']
name=str(input('Enter name of month-'))

if name in A30:
    print('number of days in month',name,'are 30 days')
elif name in A31:
    print('number of days in month',name,'are 31 days')
elif name == 'february':
    print('number of days in month',name,'are 28 or 29 days')
else:
    print('enter a correct of month')
    


# In[ ]:




