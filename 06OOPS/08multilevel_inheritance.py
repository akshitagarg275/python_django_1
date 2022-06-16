class Human:
    category = "human"

    def breathe(self):
        print("I can breathe..")


class Employee(Human):
    company = "ABC"

    def breathe(self):
        print("We are somehow breathing..")
    

class Programmer(Employee):
    def breathe(self):
        print("Don't have time")
    


e1 = Programmer()
e1.breathe()
print(e1.company)