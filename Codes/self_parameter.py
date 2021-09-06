class Person:
    def __init__(myself,name,age):
        myself.name = name
        myself.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
        
        