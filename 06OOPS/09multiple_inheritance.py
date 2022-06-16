class Human:
    category = "Human"

    def breathe(self):
        print("I can breathe....")

class Employee:
    company = "ABC"

    def breathe(self):
        print("Yeah , we do breathe...")


class Programmer(Human , Employee):
    language = "python"

    def __init__(self,name="NA"):
        self.name=name

    # def breathe(self):
    #     print("We hardly gets time")

e1=Programmer()
e1.breathe()

