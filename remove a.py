# Remove all the lines that contain the character `a' in a file and write it to another file.


# f=open("delhi.txt","r")
# nf=open("file-question3.txt","w")
# l=f.readlines()
# for i in l:
#     if 'a' in i:
#         i=i.replace('a','')
#         nf.write(i)
# nf.close()
# f.close()

fo=open("remove a.txt","w")
fo.write("Gaijangpou Kahmei\n")
fo.write("The above given name is the father of Chuningliu Kahmei")
fo.close()

fo=open('remove a.txt','r')
fi=open('remove a new.txt','w')
l=fo.readlines()
for i in l:
    if 'a' in i:
        i=i.replace('a','')
        fi.write(i)
fi.close()
fo.close()


