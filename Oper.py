from random import randint, random
from os import mkdir
from shutil import rmtree

NO_OF_STUDENTS = 100000
NO_OF_SCHOOLS_R = 50
NO_OF_SCHOOLS = 26
NO_OF_CLASSES = 20
NO_OF_MAX_STUDENTS = 250



rmtree("./Schools")
rmtree("./Students")

mkdir("./Schools")
mkdir("./Students")

for i in range(NO_OF_STUDENTS):
    a = str(i)
    with open(f"./Students/{'0'*(len(str(NO_OF_STUDENTS-1))-len(a))+a}.txt", "w") as f_out:
        f_out.write('0'*(len(str(NO_OF_STUDENTS-1))-len(a))+a+' '+str(randint(0,100))+' '+str(randint(0,100))+' '+str(randint(0,100)))
        b = []
        c = ""
        for j in range(NO_OF_SCHOOLS_R):
            c = '\n'+"school_" + chr(97+randint(0,NO_OF_SCHOOLS-1)) + " class_" + chr(97+randint(0,NO_OF_CLASSES-1))
            if not c in b:
                f_out.write(c)
                b.append(c)

for i in range(NO_OF_SCHOOLS):
    with open(f"./Schools/school_{chr(97+i)}.txt", "w") as f_out:
        f_out.write("school_" + chr(97+i))
        for j in range(NO_OF_CLASSES):
            f_out.write("\nclass_" + chr(97+j) + f" {NO_OF_MAX_STUDENTS} " + str(round(random(),2)) + ' ' + str(round(random(),2)) + ' ' + str(round(random(),2)))

with open("./Schools/no_place.txt", "w") as f_out:
    f_out.write("no_place\nno_place 0 0 0 0")
