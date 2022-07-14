# 12. Write a Python program to write a list to a file. 
Room404= ['Ningmei', 'Grace', 'Jian', 'Lan', 'Teresa']
with open('Room404.txt', "w") as myfile:
        for c in Room404:
                myfile.write("%s\n" % c)

content = open('Room404.txt')
print(content.read())
