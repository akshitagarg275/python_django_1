'''
FILE HANDLING
It allows us to store data in less complex strucutre

Types
Text file -> .doc , .txt , .py , .html
Binary File -> .png , .jpg , .pdf

text file: 
r -> read mode
w -> write mode
a -> append mode

binary file:
rb -> read mode
wb -> write mode

'''

file = open("./01function.py" , "r")

# print("SUCCESS") 
# print(file)

# data = file.read()
# print(data)

# while file.readline():
#     print(file.readline())
# print(file.readline())

# print(file.readlines()[0])
# print(file.readlines()[-1])

# print(file.read(10))

# file.seek(50)
# print(file.read())


file.close()

