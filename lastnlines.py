# 4. Write a Python program to read last n lines of a file.
def file_read(fname,n):
    txt=open(fname)
    lines=txt.readlines()
    print(lines)
    print()
    last_lines = lines[-n::]
    print(last_lines)
n=int(input("Enter the lines:-"))
file_read("n_lines.txt",n)

