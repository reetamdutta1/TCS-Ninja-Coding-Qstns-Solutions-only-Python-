class Employee:
    #class variable to keep count of employees
    count = 0

    def __init__(self,name):
        self.name = name
        #increases count whenever an employee is added
        Employee.count += 1
        

    def remove(self):
        #removes an employee
        print("\n{0} has been removed".format(self.name))
        Employee.count -= 1
 

    def greeting(self):
        #greets an employee
        print("\n\nhi, my name is ", self.name )

    @classmethod
    def get_count(cls):
        print("\n\nNumber of employees present: ", cls.count) 

employee1 = Employee("John")
employee1.greeting()
Employee.get_count()

employee2 = Employee("Mary")
employee2.greeting()
Employee.get_count()

employee3 = Employee("Henry")
employee3.greeting()
Employee.get_count()

print("\n\nEmployee creation complete. Let's Remove now!!")
employee1.remove()
employee2.remove()

Employee.get_count()

