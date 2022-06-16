'''
DRY-> Donot Repeat Yourself
OOPS : Object Oriented Programming System

class -> It is a blueprint of an object (Theoritical)
object -> Real world entity (Practical)

attributes -> varibales
methods -> functions

4 pillars of OOPS
-abstraction --> Hiding unnecessary details from the user

-encalpsulation -> combining attributes (variables) and methods(functions) together as one entity(class)
-inheritance -> parent(super) class --> child(derived) class 
-polymorphism -> poly (many) + morph (forms)

'''


class Employee :
    # class attributes
    company = "ABC"
    base_salary=10000

    def greet(self):
        print("Welcome onboard")
    

# creating object
e1 = Employee()
e1.greet()
# greet(e1)

# e2.greet()
# print(e1.company)

# e2=Employee()
# print(e2.company)

# print("AFTER")
# Instance attribute
# e1.company = "XYZ"
# print(e1.company)
# print(e2.company)
