'''
Iterators are objects that cn be iterated

iterator : Any object that you can traverse is an iterator. AN object which will return
data ,  one element at a time

for i in list:

Python iterator object must implemetn two special methods , 
__iter__()
__next__() 
known as iterator protocol

iterable: An object is called iterable if we can get an iterator from it, list , tuple list

iteration: repetetion of the process

'''

# my_list= [2,3,4,10,15,25]
# for i in my_list:
#     print(i)

my_list=[5,10,15]
# my_iter = iter(my_list)
# print(my_iter)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# my_list= [2,3,4,10,15,25]

# my_iter = iter(my_list)
# while True:
#     try:
#         ele=next(my_iter)
#         print(ele)
#     except StopIteration:
#         break


# Building a Custom Iterator
'''
every custom iterator must implemet __iter__() and __next__() methods
__iter__() method returns the iter object itself
__next__() method must return the next item in  sequence. On reaching the last element , it must raise
StopIteration Error
'''

class CubeNum:
    def __init__(self,limit) :
        self.limit = limit

    def __iter__(self):
        self.ele = 0
        return self

    def __next__(self):
        if self.ele <= self.limit:
            result= self.ele **3
            self.ele +=1
            return result
        else:
            raise StopIteration

cn = CubeNum(3)
# my_iter=iter(cn)
my_iter=cn.__iter__()

# print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
