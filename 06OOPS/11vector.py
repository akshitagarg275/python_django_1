# 2D -> 6i^ + 7j^
# 3D -> 6i^ + 7j^ + 8k^


from turtle import Vec2D


class Vector2D:

    def __init__(self,i,j):
        self.icap=i
        self.jcap = j

    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^")


class Vector3D(Vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap = k

    def show(self):
        print(f"{self.icap}i^ + {self.jcap}j^ + {self.kcap}k^")

v2=Vector2D(1,3)
v2.show()

v3=Vector3D(1,2,3)
v3.show()

