# def printname(name):
#     print("hello " + name)


# print(printname("singh"))    
   
##built-in function
# num =-100
# print(abs(num))   

# number =[1,2,3,4]

# def poweroftwo(num):
#     return num**2


# #using map 
# squared = list(map(poweroftwo,number))
# print(squared)

from functools import reduce
number =[1,2,3,4]

def multiply(x,y):
    return x*y


#using reduce 
squared = reduce(multiply,number)
print(squared)