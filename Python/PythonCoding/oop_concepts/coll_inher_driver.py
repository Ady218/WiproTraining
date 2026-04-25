from oop_concepts.college import College
from oop_concepts.student import Student
from oop_concepts.studentgrade import StudentGrade
from oop_concepts.teacher import Teacher

cc = int(input('College Code: '))
cn = input('College Name: ')
ci = input('College City: ')
rno = int(input('Roll no: '))
sn = input('Student Name: ')
m1 = int(input('marks 1: '))
m2 = int(input('marks 2: '))
m3 = int(input('marks 3: '))
eid = int(input('Eid: '))
tn = input('Teacher Name: ')
de = input('Dept Name: ')
bp = float(input('BP: '))

# project = College(ccode=cc, cname=cn, ccity=ci)
#
# project.welcome_message()
# project.display_college_details()

# project = Student(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn, m1=m1, m2=m2, m3=m3)

project = StudentGrade(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn, m1=m1, m2=m2, m3=m3)

project.welcome_message()       #through project i can call College variables also
project.display_college_details()
project.calculate_grade()
print(f'Roll No: {project.rollno} \t Name: {project.stuname} \nTotal: {project.calculate_total()} \nAverage: {project.calculate_average()}')
print(f'Result: {project.result} \nGrade: {project.grade}')

teach = Teacher(ccode=cc, ccity=ci, cname=cn, eid=eid, tn=tn, de=de, bp=bp)
print(f'Eid: {teach.empid} \tName: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')