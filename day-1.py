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

data = [10, 20, 20, 30, 40, 50, 60]

# Calculate:

# Mean-32.85
print(np.mean(data))
# Median-30
print(np.median(data))
# Mode-20
# print(np.mode(data))
# Range-50
range=max(data)-min(data)
print(range)
# Variance-
print(np.var(data))
# Standard deviation
print(np.std(data))
# First calculate manually, then verify using Python.
