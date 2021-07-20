'''
Modes of file
r = read only
w - write
a - append
x -create
 w -x -a - creates file if not exists
'''
import os


file_path = "Output.txt"
list = []

if os.path.exists(file_path):
    file = open(file_path)
    print(file.read())
    for eachline in file:
        list.append(eachline)
    print(list)

else:
    print("File is not visible")
