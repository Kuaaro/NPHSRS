from typing import TextIO


class Student:
    def __init__(self, name: str, eng_score: int, pl_score: int, math_score: int, school_choice_file: TextIO) -> None:
        self.name: str = name
        self.eng_score: int = eng_score
        self.pl_score: int = pl_score
        self.math_score: int = math_score
        self.school_choice_file: TextIO = school_choice_file
        self.current_score: float = 0.0
    
    def __str__(self) -> str:
        return f"{self.name} {self.current_score}"
    
    def get_next_choice(self) -> str:
        return self.school_choice_file.readline().split()