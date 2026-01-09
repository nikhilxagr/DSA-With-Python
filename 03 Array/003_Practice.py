from array import *

val = array('i', [10, 20, 30, 40, 50])

for i in range (0,len(val)):
    print(val[i] , end=" ")
    
print("\n")

for x in val:
    print(x , end=" , ")      
    
print("\n")

# Insertion and Deletion
val.reverse()
val.insert(1,15) 
val.append(60)
val.remove(30)

for i in range (0,len(val)):
    print(val[i] , end=" ")
    
# Copying Array

copyArray = array(val.typecode , (a for a in val))
print("\nCopied array is: ")                   

copyArray.remove(40)
for i in range (0,len(copyArray)):
    print(copyArray[i] , end=" ")
    
# Slicing

slicedArray = array(val.typecode , (a for a in val))
print("\nSliced array is: ")   
                
slicedArray = val[1:4]
for i in range (0,len(slicedArray)):
    print(slicedArray[i] , end=" ")    
    
print("\nProgram executed successfully.")