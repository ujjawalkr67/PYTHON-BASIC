#Keyword Argument
def greet(**kwargs):
    if kwargs:
        print(f"hello {kwargs['name']},{kwargs['msg']}")


greet (name="singh",msg ="Good morning")


#Arbitary arguments
def greeting(*names):
    print (names)
    for name in names:
        print(f"hellow {name}")


greeting ("singh","ujju" ,"hell")
