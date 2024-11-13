from studentManagementSystem import StudentManagement
from student import Student

def total_students(classroom):
    total = sum(student.age for student in classroom.values())
    return total
    

def average_age(classroom : StudentManagement):
    total = total_students(classroom)
    if classroom:
        average = total / len(classroom) 
        return average
    else:
        return -1
    

def enrolled_students_total(classroom : StudentManagement):
    enrolment_counter = 0
    for student in classroom.values():
        if student.get_enrolment() == True:
            enrolment_counter += 1
    
    return f"There are currently {enrolment_counter} students enrolled in subjects."
