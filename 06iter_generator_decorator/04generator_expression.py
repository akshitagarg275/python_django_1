# square_list = [i for i in range(1000)]

# square_gen = (i for i in range(1000))


# A simple generator for Fibonacci Numbers
def fib(limit):
      
    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
my_gen=fib(5)
# print(next(my_gen))
# print(next(my_gen))

for ele in my_gen:
    print(ele)