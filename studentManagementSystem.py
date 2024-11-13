from student import Student

class StudentManagement:
    """_summary_
    """
    def __init__(self):
        self.classroom = {}
        
        
    def add_student(self, student_id: int, first_name: str, last_name: str, age: int, grade: str):
        """_summary_

        Args:
            student_id (int): _description_
            first_name (str): _description_
            last_name (str): _description_
            age (int): _description_
            grade (str): _description_
        """
        for sid in self.classroom:
            if sid == student_id:
                print("This student is already in the classroom. Please add a student that is not already in this classroom.")
                return
        students = Student(student_id, first_name, last_name, age, grade)
        self.classroom[student_id] = students
        print("Student added successfully.")
        
    
    def delete_student(self, student_id: int):
        """_summary_

        Args:
            student_id (int): _description_
        """
        if student_id in self.classroom:
            self.classroom.pop(student_id)
            print(f"Student {student_id} has been successfully deleted.")
        else:
            print(f"Student {student_id} was not found.")
        
        
    def update_details(self, student_id: int, enrolment: bool, first_name = None, last_name = None, age = None, grade = None):
        """_summary_

        Args:
            student (Student): _description_
        """
        student_of_class = self.classroom.get(student_id)
        
        if not student_of_class:
            print("This is not a student of this classroom.")
            return
        
        if first_name is not None:
           student_of_class.set_first_name(first_name)
        if last_name is not None:
            student_of_class.set_last_name(last_name)
        if age is not None:
            student_of_class.set_age(age)
        if grade is not None: 
            student_of_class.set_grade(grade)
        student_of_class.set_enrolment(enrolment)
        print(f"Student {student_id} details has been successfully updated.")
        
    
    def view_class_details(self):
        print()