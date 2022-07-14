# 5. Write a Python program to read a file line by line and store it into a list.
def store_list(fname):
    with open("n_lines.txt","r") as f:
        content=f.readlines()
        print(content)
store_list("n_lines.txt")