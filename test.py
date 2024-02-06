#!/usr/bin/python3
from models import storage
from models.student import Student
from models.school import School

sc = School(name="unilag", phone_number="1362781", admin_name="qr") 
sc.save()
st = Student(first_name="Ibrahim", last_name="Ajibose", password="12345", school_id=sc.id)
st.save()
associated_school = st.school
school_name = associated_school.name
print(school_name)
associated_students = sc.students
print(sc.students)
for student in associated_students:
    print(student.id)
