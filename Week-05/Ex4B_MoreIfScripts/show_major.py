#Stephanie Y. Lopez Chavoya
student_name = "Stephanie"
student_major = "The"

if student_major == "BIOL":
    major_name = "Biology"
    office_location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major_name = "Computer Science"
    office_location = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    office_location = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    office_location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major_name = "Marketing"
    office_location = "Westly Hall, Room 310"
else:
    major_name = "Please enter valid major name."
    office_location = ""

print(f"Student: {student_name}, Major: {major_name}, ASC: {office_location}")