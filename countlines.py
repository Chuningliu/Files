# 9. Write a Python program to count the number of lines in a text file
f=open("n_lines.txt","r")
a=f.read()
b=a.split("\n")
count=0
for i in b:
        if i:
            count+=1
print(count)
f.close()


























# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
# print("Number of lines in the file: ",file_lengthy("n_lines.txt"))