from School import School
from typing import Dict, List
from Student import Student
from os import listdir

schools: Dict[str, School] = {}
school_names = listdir("./Schools")
for sch in school_names:
    temp = School("./Schools/"+sch)
    schools.update({temp.name: temp})

students: List[Student] = []
student_names = listdir("./Students")
for std in student_names:
    students.append(Student("./Students/" + std))

while students:
    students[0].get_next_choice()
    if not students[0].current_school_choice:
        schools["no_place"].class_list["no_place"].student_list.append(students[0])
        students[0].current_score = 0
        students.pop(0)
    elif students[0].current_school_choice in schools and students[0].current_class_choice in schools[students[0].current_school_choice].class_list: #Checks, if students has given the correct names of school and class 
        students.extend(schools[students[0].current_school_choice].class_list[students[0].current_class_choice].add_student(students[0])) #Adds student to classroom, if there are any students that don't meet requirements anymore adds them to list students
        students.pop(0)

with open("./results.txt", "w") as f_out:
    for school in schools.keys():
        print(schools[school])
        f_out.write(str(schools[school]) + '\n')