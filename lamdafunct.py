#without lamda function
def double(x):
    return x*2

print (double(5))

#with lamda function
doublee = lambda x:x*2
print(doublee(5))

#lamda is extensively use with map,filter ,reduce bulit-in function
lst=[1,2,3,4,5]
even_lst=list(filter(lambda x : (x%2==0) , lst))
print(even_lst)

lst2=[1,2,3,4,5]
new_lst=list(map(lambda x :x**2 , lst2))
print(new_lst)


from functools import reduce
lst3=[1,2,3,4,5]
product=reduce(lambda x,y :x*y , lst3)
print(product)