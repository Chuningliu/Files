# 2. Write a Python program to read first n lines of a file. 
file = open("read.txt","r")
lines =2
for i in range(lines):
    line = file.readline()
    print(line)