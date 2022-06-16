'''
Inheritance - >

single Inheritance

'''

class Employee:
    company = "ABC"

    @staticmethod
    def greet():
        print("WELCOME")

class Programmers(Employee):
    language = "Python"

    def __init__(self,n) :
        self.name= n


    def show(self):
        print("we are the programmers")


e1=Programmers("John")
print(e1.company)
e1.greet()


