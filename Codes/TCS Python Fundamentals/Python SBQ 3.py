class Person:
    
    def __init__(self,name,address,gender):
        self.name = name
        self.address = address
        self.gender = gender
        
        

    def countVowels(self):
        vowels = 0
        for i in self.name:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U' ):
                vowels = vowels + 1
        print("Count Of Vowels in Name = ", vowels)

 

    def countDigits(self):
        digits = 0
        for i in self.address:
            if(i.isdigit()):
                digits = digits + 1
        print("Count Of Digits in Vowels = ", digits)

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

