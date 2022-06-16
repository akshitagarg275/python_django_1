class num:

    def __init__(self,n):
        self.num=n

    def __add__(self,other):
        return self.num + other.num

    def __str__(self):
        return (f"num is {self.num}")

n1=num(3)
n2=num(6)

# print(n1+n2)
print(n1)