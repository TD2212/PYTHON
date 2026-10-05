import pandas as pd
import numpy as np


# Today learn only:

# Mean- Mean is the average on the data sert
# Median- median is the range of the starting values to the average how far they
# Mode- the repeted data are told as the mode
# Range- range is the starting value and the ending values distance
# Variance-variance is the mean divided by the n number
# Standard deviation-mean minus mode divided by the n nubmer

# Understand why ML needs statistics, not just formulas.

# Practice

# Given:

# data = [10, 20, 20, 30, 40, 50, 60]

# # Calculate:

# # Mean-32.85
# print(np.mean(data))
# # Median-30
# print(np.median(data))
# # Mode-20
# # print(np.mode(data))
# # Range-50
# range=max(data)-min(data)
# print(range)
# # Variance-
# print(np.var(data))
# # Standard deviation
# print(np.std(data))
# # First calculate manually, then verify using Python.

# #prectise

# Variables- variable is the contener of the storing the data
# Numbers - number is the int
# Strings - strings means the stores the characters 
# Lists - list is the store the multiple type of the data type in one 
# if/else - if else condition statement true or false for the 
# for loop - for loop is iteration of the array 
# Functions - functions there are two type of the function user define and default 
# Coding 

# Write these:

# # 1. Even/odd
# a=int(input("Enter a number"))
# if a%2==0:
#     print("It's a even number",a)
# else:
#     print("The number is odd",a)
# 2. Positive/negative
# a=int(input("Enter a number"))
# if a>=0:
#     print("It's positive number",a)
# else:
#     print("It's negetive number",a)
# 3. Largest number
a=[12,3,4,3,42,545]
# print(max(a))
# 4. Sum of list
# print(sum(a))
# 5. Find number in list
# i=int(input("Enter a number"))
# if i in a:
#     print("The number "a ,x"and you enter ",i)
# else:
#     print("The number is not in the list {i}")
# 6. Count numbers
# print(len(a))
# 7. Find duplicates\
duplicates = []

for i in a:
    if a.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate numbers:", duplicates)
        