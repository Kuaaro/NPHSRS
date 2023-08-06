from random import randint, random
from os import mkdir, listdir
from shutil import rmtree

#NOTE: generator creates all schools with equal number of classes and classes with equal number of possible places within them

#CONSTANTS
NO_OF_STUDENTS = 1000   #Number of students in recrutation
NO_OF_SCHOOLS_R = 5     #Number of schools and classes that students "put" on their lists
NO_OF_SCHOOLS = 5       #Number of schools to generate
NO_OF_CLASSES = 6       #Number of classes to generate
NO_OF_MAX_STUDENTS = 32 #Number of students in each class

#clearing functions

def rm_dirs():
    temp = listdir()
    if "Schools" in temp:
        rmtree("./Schools")
    if "Schools" in temp:
        rmtree("./Students")

def mk_dirs():
    mkdir("./Schools")
    mkdir("./Students")

# Functions for creating students

def make_file_name(i: int) -> str:
    file_name = str(i)
    file_name = '0'*(len(str(NO_OF_STUDENTS-1))-len(file_name))+file_name #makes name in regex format 0.*i, where its lenght is equal to lenght of NO_OF_STUDENTS-1
    return file_name

def random_score() -> str:
    return str(randint(0,100))

def ran_letter(i: int) -> str:
    return chr(97 + randint(0, i-1))

def random_school_w_class() -> str:
    return "school_" + ran_letter(NO_OF_SCHOOLS) + " class_" + ran_letter(NO_OF_CLASSES) # returns string in regex format "school_[a-z] class_[a-z]", dependent on NO_SCHOOLS and NO_CLASSES

def create_students():
    for i in range(NO_OF_STUDENTS):
        file_name = make_file_name(i)
        with open(f"./Students/{file_name}.txt", "w") as f_out:
            f_out.write(file_name+' '+random_score()+' '+random_score()+' '+random_score()) #creates first line in file in format "{name} {score} {score} {score}"
            applied_classes = []
            for j in range(NO_OF_SCHOOLS_R):
                currently_applied_class = random_school_w_class()
                if not currently_applied_class in applied_classes:
                    f_out.write('\n' + currently_applied_class)
                    applied_classes.append(currently_applied_class)

# Functions for creating schools

def create_school_name(i: int) -> str:
    return "school_" + chr(97+i)

def create_weigts() -> str:
    return str(round(random(),2))

def create_class_data(i: int) -> str:
    return f"class_{chr(97+i)} {NO_OF_MAX_STUDENTS} {create_weigts()} {create_weigts()} {create_weigts}"

def create_schools():
    for i in range(NO_OF_SCHOOLS):
        school_name = create_school_name(i)
        with open(f"./Schools/{school_name}.txt", "w") as f_out:
            f_out.write(school_name)
            for j in range(NO_OF_CLASSES):
                f_out.write('\n' + create_class_data(j))

    with open("./Schools/no_place.txt", "w") as f_out: #artificially created school w/ 1 class, where all people who don't have a place somewhere else go
        f_out.write("no_place\nno_place 0 0 0 0")

if __name__ == "__main__":
    rm_dirs()
    mk_dirs()
    create_students()
    create_schools()