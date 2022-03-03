'''To find the HCF of numbers'''
def ComputeHCF(a,b):
    """ hcf of two numbers"""
    smaller =0
    if a > b:
        smaller=b
    else :
        smaller = a

    hcf =1
    for i in range (1,smaller +1):
        if(a % i ==0) and (b % i == 0):
            hcf =i

    return hcf 


num1 =98
num2 = 78
print (f"HCF of {num1} and {num2} is : {ComputeHCF(num1,num2)}")               
print(ComputeHCF.__doc__)