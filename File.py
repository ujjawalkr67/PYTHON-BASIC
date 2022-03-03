# import os


# try:
#  f=open("example.txt",'r')
#  print(f.read())
 
# finally:
#  f.close()


#import os
#os.rename("example.txt","new.txt") 
#os.remove("example.txt")

import sys
lst =['b',0,1]
for entry in lst:
 try :
    print("the entrry is ",entry)
    r =1/int (entry)
 except:
     print ("oops!",sys.exc_info()[0],"occured")
     print("next entry")   

print("the reciprocal of",entry,"is",r)     