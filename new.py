# f=open("new.txt","w")
# f.write("my name is Ning and m doing file")
# print(f)
f=open("new.txt","r")
a=f.read()
b=a.split()
# print(b)
count=0
for i in b:
    # if i[0]=="n" or i[0]=="N":
    if "n" in i:
        count+=1
        # print(i)
print(count)
f.close()