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

# file = open("./01function.py" , "r")

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


# file.close()


# TODO: writing in a file
# file = open('./test.txt','w')
# file.write("Hello , we are writing using progrma")
# file.write("Python")
# file.close()


# TODO: append mode 
# file = open("./test.txt","a")
# file.write(" Hey there!")
# file.close()


# TODO: copy text from one file to another
# f1=open("./01function.py","r")
# f2=open("./copy.text",'w')


# for data in f1.readlines():
#     f2.write(data)

# f1.close()
# f2.close()



# TODO: binary mode

# file = open("./pic.jfif","rb")

# print(file.read())

# file.close()

# TODO: smarter way to open a file , which is scope based

# with open("./test.txt","r") as f1:
#     print(f1.read())




with open("./pic.jfif","rb") as f1 , open("copy.jfif","wb") as f2:
    data=f1.read()
    f2.write(data)
    print('SUCCESS')




