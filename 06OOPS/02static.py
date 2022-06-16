'''
if a method in your class is static i.e, it is independent of the object 
calling the function then we make it static method which is independent of object calling it
'''

class Employee:

    @staticmethod
    def greet():
        print("Welcome")


e1=Employee()
e2=Employee()

e1.greet()
e2.greet()