# 14. Write a Python program to combine each line from first file 
# with the corresponding line in second file. 
with open('n_lines.txt') as f1, open('Room404.txt') as f:
    for line1, line2 in zip(f1, f):
        print(line1+line2)