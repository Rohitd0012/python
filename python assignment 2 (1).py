#!/usr/bin/env python
# coding: utf-8

# ###### '''Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary'''

# In[55]:


salary=float(input("Ramesh's Basic salary-"))

#dearness allowance is 40% of Basic salary 
dearnes_allowance=0.4*salary

#house rent allowance is 20% of basic salary
house_rent_allowance=0.2*salary

#gross salary is sum of basic salary,dearness allowance and house rent allowance
gs=salary+dearnes_allowance+house_rent_allowance

print("Ramesh's Gross salary" , gs,'Rupees')


# ##### The distance between two cities (in km.) is input through the keyboard. Write a program to convert and print this distance in meters, feet, inches and centimeters.

# In[18]:


d=float(input("the distance between two cities (in km.)"))

#1km=1000 meter
dm=d*1000

#1meter=100 centi meter
dcm=dm*100

#1 inch = 2.54 centi meter 
di=dcm/2.54

# 1 feet = 12 inch 
dft=di/12

print('distance in meter',dm,'m')
print('distance in centimeter',dcm,'cm')
print('distance in inch',di,'inch')
print('distance in dft',dft,'feet')


# #### If the marks obtained by a student in five different subjects are input through the keyboard, find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by a student in each subject is 100.
# 

# In[58]:


s1=int(input('mark of subject 1-'))
s2=int(input('mark of subject 2-'))
s3=int(input('mark of subject 3-'))
s4=int(input('mark of subject 4-'))
s5=int(input('mark of subject 5-'))

total_marks=500
total_obtained_marks=s1+s2+s3+s4+s5

print("aggregate marks=",total_obtained_marks)
per=((total_obtained_marks/total_marks)*100)

print('Percentage marks by students=',per,'%')



# ###### Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to convert this temperature into Centigrade degrees.

# In[29]:


t=float(input("The Temperature of City in Fahrenheit="))
#1 centigrade degree=33.8 Fahrenheit degree
t1=(t/33.8) 
print('The Temperature of City in Celsius degree',t1)


# ###### The length & breadth of a rectangle and radius of a circle are input through thekeyboard. Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.
# 

# In[54]:


import math
l=float(input('The Length of Rectangle in meter='))
b=float(input('the breadth of Rectanglein meter='))
r=float(input('the Radius of Circle in meter='))

#formula for Area of Rectangle=length * breadth
A=(l*b) 
print('the Area of Rectangle is',A,'sq.m')

 #formula for Perimeter of Rectangle=2*length+2*breadth
P=(2*l+2*b)
print('The Perimeter of Rectangle is',P,"meter")

 #formula for Circumference of Circle=2*pi(3.14)*radius
c=2*math.pi*r
print('the circumference of Circle is',c,'meter')

#formula for area of circle =pi*radius*radius
a=math.pi*r*r 
print('the area of Circle is',a,"sq.m")




# #### Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D.
# 

# In[66]:


a=int(input("Enter the A Values:"))
b=int(input("Enter the B Values:"))
print("Before A Values : ",a)
print("Before B Values : ",b)
d=a
c=b
print("After C Values:",c)
print("After D Values:",d)


# ###### If a five-digit number is input through the keyboard, write a program to calculate the sum of its digits. ( Hint: Use the modulus operator '%')

# In[ ]:





# ###### 8. If a five-digit number is input through the keyboard, write a program to reverse the number.
# 

# In[4]:


N=int(input('enter five digit number-'))
print(str(N)[::-1])


# ###### If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number.

# In[5]:


n1=input('enter 4 digit number-')


# ###### In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population, write a program to find the total number of illiterate men and women if the population of the town is 80,000.

# In[8]:


#population of town is 80000
p=80000
#population of men is 52 %
pmen=(0.52*p)
pw=(p-pmen)
p_lit=(0.48*p)
pm_lit=(.35*pmen)
pw_lit=(p_lit-pm_lit)
p_w_il=(pw-pw_lit)
p_men_ill=(pmen-pm_lit)
print('total number of illiterate men is-',p_men_ill)
print('total number of illiterate women is-',p_w_il)


# ###### A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.

# In[ ]:





# ###### If the total selling price of 15 items and the total profit earned on them is input through the keyboard, write a program to find the cost price of one item.

# In[10]:


sp=float(input('selling price of items-'))
profit=float(input('profit earned on them-'))
cp=sp-profit
#cost of each item 
cp=cp/15
print('cost price of one item is', cp)


# ###### While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

# In[15]:


qty=int(input('enter quantity purchased'))
price=float(input('enter price of item'))
exp=qty*price
if qty>10:
    exp1=(exp-(exp*.1))
    print('total expenses',exp1)
else:
    print('total expenses',exp)


# ###### The current year and the year in which the employee joined the organization are entered through the keyboard. If the number of years for which the employee has served the organization is greater than 3 then a bonus of Rs. 2500/- is given to the employee. If the years of service are not greater than 3, then the program should do nothin

# In[17]:


# current year entered through keyboard
yr=int(input('enter current year-'))

# joining year entred through keyboard
j_yr=int(input('enter joining year of employee-'))

#service year of employee
s_yr=yr-j_yr
if s_yr>3:
    print('he/she completed',s_yr,'years in compony, so he/she will get bonus of 2500 rupees')


# ###### . If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the employee's salary is input through the keyboard write a program to find his gross salary

# In[20]:


# basic salary is entered through keyboard
b_salary=int(input('enter a basic salary of employee'))

if b_salary<1500:
    hra=(b_salary*0.1)
    da=(b_salary*0.9)
    gs=(b_salary+hra+da)
    print('gross salary of employee is',gs)
# if salary is greater than or equal to 1500 rupees
elif b_salary>=1500:
    hra=500
    da=(b_salary*0.98)
    gs=(b_salary+hra+da)
    print('gross salary of employee is',gs)
    
    


# ###### The marks obtained by a student in 5 different subjects are input through the keyboard. 
# The student gets a division as per the following rules: 
# Write a program to calculate the 
# division obtained by the student.
# 
# a. Percentage above or equal to 60 - First division
# 
# b. Percentage between 50 and 59 - Second division
# 
# c. Percentage between 40 and 49 - Third division
# 
# d. Percentage less than 40 – Fail

# In[34]:


# marks obatined in 5 subjects
s1=float(input('marks in subject 1-'))
s2=float(input('marks in subject 2-'))
s3=float(input('marks in subject 3-'))
s4=float(input('marks in subject 4-'))
s5=float(input('marks in subject 5-'))
total_marks=(s1+s2+s3+s4+s5)
per=(total_marks/500)*100
if per >=60:
    print('student get',per,'% and First division')
elif (per>=50 and per<=59):
    print('student get',per,'% and second division')
elif (per>=40 and per<=49):
    print('student get',per,'% and third division')
else:
    print('student fails',per,'%')



# ###### A company insures its drivers in the following cases:
# a. If the driver is married.
# 
# b. If the driver is unmarried, male & above 30 years of age.
# 
# c. If the driver is unmarried, female & above 25 years of age

# In[41]:


status=str(input('driver is married (yes/no)- ' ))
sex=str(input('diver is male (yes/no)- ' ))
age=int(input('age of driver is ' ))
if status==('yes'):
    print('company insure the driver')
elif status=='no' and sex=='yes' and age>30:
    print('company insure the driver')
elif status=='no' and sex=='no' and age>25:
    print('company insure the driver')
else:
    print('company will not insure driver')


# In[ ]:


# # Write a program to calculate the salary as per the following table: -->
# Gender Year of Service Qualifications Salary
# Male >= 10 Post - Graduate 15000
# >= 10 Graduate 10000
# < 10 Post - Graduate 10000
# < 10 Graduate 7000
# Female >= 10 Post - Graduate 12000
# >= 10 Graduate 9000
# < 10 Post - Graduate 10000
# < 10 Graduate 6000


# In[45]:


gender=str(input('gender of employee (m/f)-'))
yos=int(input('service year-'))
edu=str(input('qualification (p/g)'))
if gender=='m' and yos>= 10 and edu=='p':
    print('salary of employee is 15k')
elif gender=='m' and yos>=10 and edu=='g':
    print('salary of employee is 10k')
elif gender=='m' and yos<10 and edu=='p':
    print('salary is 10k')
elif gender=='m' and yos<10 and edu=='g':
    print('salary is 7k')
elif gender=='f' and yos>= 10 and edu=='p':
    print('salary of employee is 12k')
elif gender=='f' and yos>=10 and edu=='g':
    print('salary of employee is 9k')
elif gender=='f' and yos<10 and edu=='p':
    print('salary is 10k')
elif gender=='f' and yos<10 and edu=='g':
    print('salary is 6k')



# ###### If cost price and selling price of an item is input through the keyboard, write a program to determine whether the seller has made profit or incurred loss. Also determine how much profit he made or loss he incurred.

# In[49]:


cp=float(input('cost price of item is '))
sp=float(input('selling price of item is '))
# when cost price is greater than selling price then seller will make a loss 
if cp>sp:
    l=cp-sp
    print('seller has made a loss of',l,'rupees')
# when cost price is less than selling price then seller will make a profit
elif cp<sp:
    p=sp-cp
    print('seller has made a profit of',p,'rupees')
else:
    print('cost to cost')


# ###### Any integer is input through the keyboard. Write a program to find out whether it is an odd number or even number. (Hint: Use the % (modulus) operator)

# In[51]:


n1 = int(input("Enter the Number-"))
if(n1%2==0):
    print(n1,"is Even Number")
else:
 
  print(n1,"is Odd Number")


# ###### If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.
# 

# In[11]:


Ar=float(input('age of ram is '))
As=float(input('age of shyam is '))
Aa=float(input('age of ajay is '))

if Ar<As and Ar<Aa:
    print('Ram is youngest and his age is',Ar,'years old')
elif As<Ar and As<Aa:
    print('Shyam is youngest and his age is',As,'years old')
else:
    print('Ajay is youngest and his age is',Aa,'years old')


# ###### Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

# In[15]:


a=int(input('angle of a '))
b=int(input('angle of b '))
c=int(input('angle of c '))

if (a+b+c)==180:
    print('a triangle is valid')
else:
    print('a triangle is not valid')



# ###### Find the absolute value of a number entered through the keyboard.
# 

# In[21]:


n1=int(input('number is '))
if n1>0:
#     absolute value means each number is same unit far from 0
    n2=((-1)*n1)
    print('absolute value of a number',n1,'is',n2)


# ###### Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 and breadth = 4 is greater than its perimeter

# In[26]:


l=float(input('length of rectangle is '))
b=float(input('breadth of rectangle is'))

a=l*b
p=(2*l+2*b)
if a>p:
    print('the area of the rectangle with length =',l,' and breadth =',b,'is greater than its perimeter')


# ###### Any year is entered through the keyboard, write a program to determine whether the year is leap or not. Use the logical operators && and ||

# In[28]:


yr = int(input("Enter the Year ")) 
if (yr%4 == 0 and yr%100 != 0) or (yr%400 == 0):
    print("Given Year is a leap Year")
else:  
    print ("Given Year is not a leap Year")  


# ###### A certain grade of steel is graded according to the following conditions:
# i. Hardness must be greater than 50
# ii. Carbon content must be less than 0.7
# iii. Tensile strength must be greater than 5600
# 
# The grades are as follows:
# i. Grade is 10 if all three conditions are met
# ii. Grade is 9 if conditions (i) and (ii) are met
# iii. Grade is 8 if conditions (ii) and (iii) are met
# iv. Grade is 7 if conditions (i) and (iii) are met
# v. Grade is 6 if only one condition is met
# vi. Grade is 5 if none of the conditions are met
# 
# Write a program, which will require the user to give values of hardness, carbon content and 
# tensile strength of the steel under consideration and output the grade of the steel.

# In[36]:


h=int(input('enter hardness of steel '))
cc=float(input('enter carbon content of steel '))
ts=int(input('enter tensile strength of steel '))

if h>50 and cc<0.7 and ts>5600:
       print('the grade of steel is 10')
elif  h>50 and cc<0.7:
       print('the grade of steel is 9')
elif  cc<0.7 and ts>5600: 
        print('the grade of steel is 8')
elif h>50 and ts>5600:
       print('the grade of steel is 7')
elif h>50 or cc<0.7 or ts>5600 :
       print('the grade of steel is 6')
       
       


# ###### . A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days your membership will be cancelled. Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message.
# 

# In[42]:


d=int(input('enter a days to return '))

if d<=5:
    print('you returned book after',d,'you have to pay fine of 50 paise')
elif d<=10 and d>=6:
    print('you returned book after',d,'you have to pay fine of 1 rupee')
elif d>=10 and d<=30:
     print('you returned book after',d,'you have to pay fine of 5 rupees')
else:
     print('you returned book after',d,'your membership is cancelled')


# In[ ]:




