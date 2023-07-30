from typing import List
from Student import Student

class School:
    def __init__(self, name: str, eng_mult: float, pl_mult: float, math_mult: float) -> None:
        self.name = name
        self.eng_mult = eng_mult
        self.pl_mult = pl_mult
        self.math_mult = math_mult
        self.student_list: List[Student]= []
    
    def add_student(self, student: Student) -> Student:
        student.current_score = self.eng_mult * student.eng_score + self.pl_mult * student.pl_score + self.math_mult * student.math_score

        for i in range(len(self.student_list)):
            if student.current_score > self.student_list[i].current_score:
                self.student_list.insert(i, student)

                print(self)

                if len(self.student_list) > 10:
                    return self.student_list.pop()
                return None
            
        print(self)

        if len(self.student_list) < 10:
            self.student_list.append(student)
            return None
        return student

    def __str__(self) -> str:
        return self.name + ":\n\t" + "\n\t".join([str(x) for x in self.student_list])
            