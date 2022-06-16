class Calculator:
    '''It performs calculations'''

    def __init__(self,num):
        self.num=num

    def cube(self):
        return self.num**3

    def square(self):
        return self.num**2

obj = Calculator(5)
print(obj.cube())
print(obj.square())