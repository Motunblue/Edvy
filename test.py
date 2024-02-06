#!/usr/bin/python3
from models import storage
from models.student import Student
from models.school import School

sc = School(name="unilag", phone_number="1362781", admin_name="qr", id="unilag-12462") 
sc.save()
st = Student(school_id=sc.id, first_name="Ibrahim", last_name="Ajibose", password="i1234")
st.save()
