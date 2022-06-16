class Employee:

    def __init__(self , name):
        self.name=name
    
    @property
    def show(self):
        return self.name

    @show.setter
    def show(self,val):
        self.name=val


e1=Employee("John")
print(e1.show)

# e1.changeName("Jane")
e1.show="jane"
print(e1.show)