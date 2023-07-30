from typing import List
from Student import Student

class Class:
    def __init__(self, name: str, no_students: int, math_mult: float, pl_mult: float, eng_mult: float) -> None:
        self.name = name
        self.no_students = no_students
        self.student_list: List[Student] = []
        self.math_mult = math_mult
        self.pl_mult = pl_mult
        self.eng_mult = eng_mult