
file1 = open('test_file.txt', 'r')
print(file1.read())

#for i in range(5):
#     file1.write("This is line %d\r" %(i+1))

file1.close()


# Python code to illustrate context manager
with open("test_file.txt") as file:
    contents = file.read()
print(contents)


with open("test_file.txt") as file:
    contents = file.readline()
    contents = contents + file.readline ()
    contents = contents + file.readline ()
    contents = contents + file.readlines()
print(contents)
