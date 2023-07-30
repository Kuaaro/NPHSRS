from Student import Student
from School import School
from typing import List

students: List[Student] = []
students.append(Student('A', 54, 53, 26))
students.append(Student('B', 76, 87, 53))
students.append(Student('C', 23, 13, 89))
students.append(Student('D', 13, 83, 35))
students.append(Student('E', 63, 83, 97))
students.append(Student('F', 27, 37, 37))
students.append(Student('G', 94, 26, 74))
students.append(Student('H', 37, 53, 18))
students.append(Student('I', 30, 95, 76))
students.append(Student('J', 20, 37, 54))

schools: List[School] = []
schools.append(School("HS1", 0.4, 0.4, 0.2))
schools.append(School("HS2", 0.3, 0.3, 0.4))

for student in students:
    temp = schools[0].add_student(student)
    if type(temp) == Student:
        schools[1].add_student(temp)
print(schools[0])
print(schools[1])