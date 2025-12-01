''' You are creating a system for a school to manage student records. Each student has:

A name
An age
A grade
A roll number

Instead of writing separate variables for each student, you decide to create a class called Student to represent the blueprint for any student.
By using a class, you can create multiple student records quickly and manage them efficiently.

Objective
Define a class called Student.
Use attributes (name, age, grade, roll number).
Create multiple student objects.
Display each student’s information using a method.'''


class student:
    def __init__(self,name,age,grade,roll_number):
        self.name=name
        self.age=age
        self.grade=grade
        self.roll_number=roll_number
        
    def student_info(self):
        print("student name: ",self.name)
        print("student age: ",self.age)
        print("student grade: ",self.grade)
        print("student roll_number: ",self.roll_number)
        
s1=student("yuva",24,"A",25)
s1.student_info()

s2=student("charan",25,"A",3)
s2.student_info()

s3=student("ranjith",20,"B",19)
s3.student_info()
    
