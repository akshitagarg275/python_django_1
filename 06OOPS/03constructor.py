'''
__init__(): -> which acts like a constructor . 
A constructor is a special function which gets called as soon as an object is created for a class

'''

class Employee:
    company="ABC"

    def __init__(self,n,a) :
        # print("Constructor is called")
        self.name= n
        self.age=a
    
    def getProfile(self):
        print(f"name is {self.name} and age is {self.age}")


e1=Employee("John",25)
e2=Employee("Jane",24)

e1.getProfile()
e2.getProfile()


    