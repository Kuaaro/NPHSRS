from typing import Dict
from Class import Class

class School:
    def __init__(self, school_file) -> None:
        with open(school_file, "r") as f_in:
            self.name: str = f_in.readline().rstrip('\n')
            if self.name == None:
                self = None
                return

            self.class_list: Dict[str, Class] = {}

            while read_line := f_in.readline():
                temp: Class = Class(read_line)
                self.class_list.update({temp.name: temp})

    def __str__(self) -> str:
        return self.name + ":\n\t" + "\n\t".join([str(x) for x in self.class_list.values()])