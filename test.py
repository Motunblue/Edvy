#!/usr/bin/python3
from models import storage
from models.student import Student
from models.school import School
from models.staff import Staff
from models.post import Post

sc = School(name="unilag", phone_number="1362781", admin_name="qr", password="123") 
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

stf = Staff(first_name="Ibrahim", last_name="Ajibose", password="12345", profession="accountant", phone_number="123344", school_id=sc.id)
stf.save()
associated_school = stf.school
school_name = associated_school.name
print(school_name)

associated_staffs = sc.staffs
for staff in associated_staffs:
    print(staff.id)

post = Post(title="A title", content="The content", student_id=st.id, school_id=sc.id)
post.save()

post = Post(title="A title", content="The content", staff_id=stf.id, school_id=sc.id)
post.save()

post = Post(title="The second title", content="The Second content", student_id=st.id, school_id=sc.id)
post.save()

student_post = st.posts
for post in student_post:
    print(post.title)
