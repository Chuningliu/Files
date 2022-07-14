# Write a program that reads a text file and count the number of words ending with “ing”.
# f=open("ing.txt","w")
# f.write("I love eating,sleeping,walking,running,working except talking")
# f.close()
# fo=open('remove a.txt','r')
# fi=open('remove a new.txt','w')
# l=fo.readlines()
# for i in l:
#     if 'a' in i:
#         i=i.replace('a','')
#         fi.write(i)
# fi.close()
# fo.close()


f=open("ing.txt","r")
b=a.split()
print(b)
for i in b:
    if "a" in i:
        i=i.replace("a","")
print(i)
f.close()


# a=f.read()
# b=a.split()
# # print(b)
# count=0
# for i in b:
#     if "ing" in i:
#         count+=1
# print(count)

# a=f.read()
# b=a.split()
# # print(b)
# for i in b:
#     if "ing" in i:
#         b.remove()
# print(b)


    

