from io import TextIOWrapper
from typing import List
from linecache import getline

class Student:
    def __init__(self, school_choice_file: str) -> None:
        self.school_choice_file = school_choice_file
        self.current_school_choice: List[str] = getline(school_choice_file, 1).rstrip('\n').split(' ') #First version was using open(), but test at 10000 students crashed
        
        self.id = self.current_school_choice[0]
        self.math_score = int(self.current_school_choice[1])
        self.pl_score = int(self.current_school_choice[2])
        self.eng_score = int(self.current_school_choice[3])

        self.line2read = 2
        self.current_score: float = 0.0
    
    def __str__(self) -> str:
        return f"{self.id}: {self.current_score}"
    
    def get_next_choice(self) -> None:
        temp = getline(self.school_choice_file, self.line2read).rstrip('\n').split(' ')

        if temp[0]:
            self.current_school_choice = temp[0]
            self.current_class_choice = temp[1]
            self.line2read += 1
        else:
            self.current_school_choice = ""
            self.current_class_choice = ""