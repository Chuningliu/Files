# Take a sample of ten phishing e-mails (or any text file)
# and find most commonly occurring word(s)

fo=open("email.txt","w")
fo.write("gaijangpou @gmail.com\n")
fo.write("chuningliukahmei @gmail.com\n""abama @gmail.com")
fo.close()

fo=open('email.txt','r')
a=fo.read()
b=a.split()
count=0
for i in b:
    for j in b:
        if i==j:
            c=j
            count+=1
print(c)


 



























