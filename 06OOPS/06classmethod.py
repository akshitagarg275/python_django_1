class Employee:
    company = "ABC"

    # def change(self):
    #     self.__class__.company = "XYZ"

    @classmethod
    def change(cls , name):
        cls.company=name


e1 = Employee()
Employee.change("PQR")
# e1.change()
print(e1.company)

e2=Employee()
print(e2.company)
