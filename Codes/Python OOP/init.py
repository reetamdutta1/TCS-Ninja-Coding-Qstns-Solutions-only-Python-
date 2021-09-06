class Person:
    def __init__(self,name):
        print("InitiALized")
        self.name = name
        pass

    def message(self):
        print("Hi, I am {0}".format(self.name))

p=Person("Reetam")
p.message()