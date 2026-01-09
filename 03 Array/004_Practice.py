# UserInput

from array import *

arr = array('i', [])

n = int(input("Enter number of elements you want to store in array: "))

for i in range(0 , n):
    x = int(input("Enter element: "))
    arr.append(x)
    
for x in arr:
    print(x , end=" , ")

    
    
    