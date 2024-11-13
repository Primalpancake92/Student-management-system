from student import Student
import student_statistics
from studentManagementSystem import StudentManagement

def making_class():
    classroom = StudentManagement()
    while True: 
        user_input = input("Enter student details for the classroom (-1 to exit): ")
        
        if user_input.strip() == "-1":
            print("Goodbye.")
        elif user_input.strip() == "done":
            return f"{classroom.get_classroom()}"
            
        token = user_input.split(" ")
        
        student_id, first_name, last_name, age, grade = token
        
        try: 
            student_id = int(student_id)
            age = int(age)

            if not (int(student_id) or int(age)) or not (int(student_id) and int(age)):
                raise ValueError("Student ID number and age must be a number. Please try again.") 
            
        except ValueError as e:
            print(e)
                
        classroom.add_student(student_id, first_name, last_name, age, grade)
        
    
        
def main():
    print(making_class())
    

if __name__ == "__main__":
    main()