batch1_students = ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj", "Shakrudin", "Tara", "Suraj", "Krishna"]
students_file = open("people4.html", "w")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("")
for student in batch1_students:
    students_file.write("" + student + "\n")
students_file.write("\n")
students_file.write("\n")
students_file.write("\n")
students_file.close()