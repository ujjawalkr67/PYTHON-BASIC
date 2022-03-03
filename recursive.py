#fibonnaci series using recursive function
def fibonacci(num):
    if num <=1:
        return num
    else:
       return  fibonacci(num-1)+fibonacci(num-2)


nterms =10
for num in range(nterms):
    print(fibonacci(num))