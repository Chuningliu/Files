# f=open("question1.txt","r")
# a=f.read()
# b=a.split()
# print(a)
# for i in b:
#     if i =="delhi":
#         f=open("delhi.txt","w")
#         f.write("imtiyaz - delhi\n""ayishah - delhi\n""karthikeyan - delhi\n""pankaj - delhi\n""siddhi - delhi\n""mohinder - delhi\n""neela - delhi\n""sarika - delhi\n""harshad - delhi\n""sekhar - delhi\n""nand - delhi\n""anoop - delhi\n""brijesh - delhi\n""govind - delhi")
#     elif i == "shimla":
#         f=open("shimla.txt","w")
#         f.write("rati - shimla\n""raghu - shimla\n""puneet - shimla\n""rajeev - shimla\n""priyanka - shimla\n""deepti - shimla")
#     else:
#         f=open("others.txt","w")
#         f.write("naseer - kanpur\n""nilima - cochin\n""trishna - raipur""salma - jaipur\n""suman - jaipur\n""rajendra - jaipur\n""sashi - jaipur\n""pradeep - jaipur\n""rishabh - meerut")
# f.close()


shimla=open("shimla.txt","a")
delhi=open("delhi.txt","a")
jaipur=open("jaipur.txt","a")
others=open("others.txt","a")
f=open("question1.txt","r")
a=f.read()
b=a.split("\n")
print(b)
i=0
while i<len(b):  
    if "delhi" in b[i]:
        delhi.write(b[i])
        delhi.write("\n")
    elif "shimla" in b[i]:
        shimla.write(b[i])
        shimla.write("\n")
    elif "jaipur" in b[i]:
        jaipur.write(b[i])
        jaipur.write("\n")
    else:
        others.write(b[i])
        others.write("\n")
    i=i+1
f.close()



        