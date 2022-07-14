# 6. Write a Python program to read a file line by line store it into a variable
def file_read(fname):
        with open (fname, "r") as myfile:
                var=myfile.readlines()
                print(var)
file_read('n_lines.txt')



