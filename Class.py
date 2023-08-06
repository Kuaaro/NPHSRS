from typing import List
from Student import Student

class Class:
    def __init__(self, class_data: str) -> None:
        temp = class_data.split(' ')

        self.name = temp[0]
        self.no_students = int(temp[1])
        self.math_mult = float(temp[2])
        self.pl_mult = float(temp[3])
        self.eng_mult = float(temp[4])

        self.student_list: List[Student] = [] #List of accepted students, sorted by score
    
    def add_student(self, student: Student) -> List[Student]:
        student.current_score = round(student.eng_score * self.eng_mult + student.pl_score * self.pl_mult + student.math_score * self.math_mult, 2)

        for i in range(len(self.student_list)):
            if self.student_list[i].current_score < student.current_score:
                self.student_list.insert(i, student)
                break
        else:
            self.student_list.append(student)

        if len(self.student_list) > self.no_students: #Checks, if there are too many students in a classroom
            temp: float = self.student_list[self.no_students-1].current_score
            for i in range(len(self.student_list)-self.no_students, len(self.student_list)):
                if temp > self.student_list[i].current_score: #Removes all students, that have scores lower, than the person on the last avalible place
                    out: List[Student] = self.student_list[i:]
                    self.student_list = self.student_list[:i]
                    return out
        return []
    
    def __str__(self) -> str:
        return self.name + ": " + str(len(self.student_list)) +  "\n\t\t" + "\n\t\t".join(["-" + str(x) for x in self.student_list])