from numpy import *

val = array([1, 2, 3, 4.5, 5])

for x in val:
    print(x , end=" ")
    
# Arithmatic Progression

val = linspace(10, 20 , 5)  # start, end, number of values
print("\n", val)    

val = arange(10, 20, 2)  # start, end, step
print(val)

val = logspace(1, 2, 5)  # 10^start to 10^end
print(val)

val = zeros(5)  # create array of zeros
print(val)

val = ones(5)  # create array of ones
print(val)

val = full(5, 7)  # create array of given value
print(val)

# 1 D and 2 D array Using numpy

zero = array(10)
print(zero)

one = array([1, 2, 3, 4, 5])
print(one)

two = array([[1, 2, 3], [4, 5, 6]])
print(two)

three = array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three)