# 1. Write a Python program to read an entire text file.
with open("read.txt",'w') as f:
        f.write("God is really creative,I mean... look at me:)")
        
    
    
    


def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('read.txt')