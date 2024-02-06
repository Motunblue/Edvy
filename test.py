#!/usr/bin/python3
from models import storage
from models.student import Student
from models.school import School

sc = School(name="unilag", phone_number="1362781", admin_name="qr") 
sc.save()
st = Student(first_name="Ibrahim", last_name="Ajibose", password="12345", school_id="UNI-0002", class_id="cls2")
st.save()
