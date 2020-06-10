import math
import numpy as np
import pandas as pd
import random

# Print out the numerical constant pi with ten digits after the decimal point using the internal constant `pi`.
round(math.pi, 10)

# Sum up the first 100 terms of the series 1 + 1/2 + 1/4 + 1/8 + ...
s = 0
for i in range(0, 99) :
  s += 1 / (2 **i)
s

# Find the product of the first 20 terms of `1/3 * 1/6 * 1/9 *` ...
p = 1
for i in range(1, 20) :
  p *= 1 / (3 * i)
p

# Find the product of the first 500 terms of `1 * 1/2 * 1/4 * 1/8 *` ...
p = 1
for i in range(0, 499) :
  p *= 1 / (2 ** i)
p

# Figure out a means to express the answer more exactly. Not compute exactly, but express more exactly.
p = 0
for i in range(-499, 0) :
  p += i * math.log(2)
p

# Create the sequence `x = [Inf, 20, 18, ..., -20]`.
x = [math.inf]
start = 20
for i in range(1, 22) :
  x.append(start)
  start -= 2
x

# Create the sequence `x = [log_3(Inf), log_3(100), log_3(98), ... log_3(-20)]`.
x = np.array([math.log(math.inf, 3)])
start = 100
for i in range(1, 62) :
  if (start < 0) :
    num = math.nan
  elif (start == 0) :
    num = -math.inf
  else :
    num = np.array([math.log(start, 3)])
  x = np.concatenate((x, num), axis = None)
  start -= 2
x 

# Create a vector of booleans where the entry is true if `x[i]` is positive and finite.
pos_reals = np.isfinite(x)

# Locate the indices of the non-numbers in this vector. 
not_pos_reals = np.isinf(x) | np.isnan(x)
[i for i, val in enumerate(not_pos_reals) if val] 

# Locate the indices of the infinite quantities in this vector.
[i for i, val in enumerate(np.isinf(x)) if val]

# Locate the indices of the min and max in this vector.
np.where(x == min(x[np.isfinite(x)]))
np.where(x == max(x[np.isfinite(x)]))

# Count the number of unique values in `x`.
len(pd.unique(x))

# Cast `x` to a factor. Do the number of levels make sense?
pd.Categorical(x)

# Cast `x` to integers.
np.int32(x)

# Use `x` to create a new vector `y` containing only real numbers.
y = x[np.isfinite(x)]

# Calculate the average of 100 realizations of standard Bernoullis in one line using the `sample` function.
bern = [0, 1]
np.mean(np.random.choice(bern, 100))

# Calculate the average of 500 realizations of Bernoullis with p = 0.9 in one line using the `sample` function.
bern = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
np.mean(np.random.choice(bern, 500))

# In class we considered a variable `x_3` which measured "criminality". We imagined L = 4 levels "none",
# "infraction", "misdimeanor" and "felony". Create a variable `x_3` here with 100 random elements 
# (equally probable). Create it as a nominal (i.e. unordered) factor.
lvl = ["none", "infraction", "misdemeanor", "felony"]
x_3 = np.random.choice(lvl, 100)
x_3 = pd.Categorical(x_3)

# Use `x_3` to create `x_3_bin`, a binary feature where 0 is no crime and 1 is any crime.
x_3_bin = (x_3 != "none")
x_3_bin = np.int32(x_3_bin)

# Use `x_3` to create `x_3_ord`, an ordered, nominal factor variable. Ensure the proper ordinal ordering.
x_3_ord = pd.Categorical(x_3, categories=lvl, ordered=True)




