# Create a binary file with roll number, name and marks.
# Input a roll number and increase the marks by 10.
import pickle
def write():
    f=open("marksupdate.txt","wb")
    while True:
        roll=int(input("Enter the Roll no.:-"))
        name=input("Enter the name of the Students:-")
        marks=int(input("Enter the marks:"))
        a=[roll,name,marks]
        pickle.dump(a,f)
        rec=input("Wanna add more Students?(Y/N)")
        if rec in "Nn":
            break
    f.close()
def Read():
    f=open("marksupdate.txt","rb")
    try:
        while True:
            b=pickle.load(f)
            print(b)
    except EOFError:
        f.close()
# def update():
#     f=open("marksupdate.txt","rb+")
#     rollnum=int(input("Enter the Roll num.:"))
#     try:
#         while True:
#             pos=f.tell() 
#             b=pickle.load(f)
#             if b[0]==rollnum:
#                 nroll=10+b[2]
#                 b[2]=nroll
#                 f.seek(pos)
#                 pickle.dump(b,f)
#             print(b)
#     except EOFError:
#         f.close()
write()
Read()
# update()
# Read()


