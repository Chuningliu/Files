f=open("question1.txt","r")
count = 0.
for line in f:
    if line != "\n":
        count += 1.
print(count)
f.close()                                                                                                                                                                          

