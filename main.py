from student import Student
import student_statistics
from studentManagementSystem import StudentManagement

def making_class():
    classroom = StudentManagement()
    while True: 
        user_input = input("Enter student details for the classroom (-1 to exit): ")
        
        if user_input.strip() == "-1":
            return classroom
        
        token = user_input.split(" ")
        
        student_id, first_name, last_name, age, grade = token
        
        try: 
            student_id = int(student_id)
            age = int(age)
            
        except ValueError:
            print("Student ID and/or age must be a number. Please try again.")
            continue
                
                
        classroom.add_student(student_id, first_name, last_name, age, grade)
        
        
def main():
    classroom = making_class()
    print(classroom)
    

if __name__ == "__main__":
    main()