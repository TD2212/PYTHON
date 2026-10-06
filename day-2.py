# 1. Python revision — 45 min

# if / elif / else
# for loops
# while loops
# Lists
# range()
# len()
# max(), min(), sum()

# Practice:

# Check whether a number exists in a list.
# a=[1,2,3,4,5,6,7,8,9,10]
# i=int(input("Enter a number"))
# if i in a:
#     print(i,"is in the list")
# else:
#     print(i,"is not in the list")

# Find the largest number without max().
a=[1,2,3,4,55,6,7,8,9]
max=a[0]
for i in a:
    if i>max:
        max=i
        
print(max) 
# Find the smallest number without min().
a=[1,2,3,4,55,6,7,8,9]
min=a[0]
for i in a:
    if i<min:
        max=i
        
print(min)
# Count even and odd numbers.
# for i in int(a):
#     if len(a)%2==0:
#         print("The even number of the list",a)
#         i=i+1
#     else:
#         print("The odd number of the list",a)
#         i=i+1
# Calculate the sum of all list elements.


# Reverse a list without .reverse().
# print(a[::-1])
# Find duplicate elements.
import numpy as np
import pandas as pd
data = [10, 20, 20, 30, 40, 50, 60]

# Calculate manually:

# Mean
print(np.mean(data))
# Median
print(np.median(data))
# Mode
# print(np.modf(data))
# Range
print(range)
# Variance
print(np.var(data))
# Standard deviation
print(np.std(data))
# Then verify using NumPy.

# After that, we'll connect the statistics to a real ML dataset.