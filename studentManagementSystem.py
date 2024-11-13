from student import Student

class StudentManagement:
    """_summary_
    """
    def __init__(self):
        self.classroom = {}
        
        
    def add_student(self, student_id: int, first_name: str, last_name: str, age: int, grade: str):
        """This is a method that takes in arguments: student_id, first_name, last_name, age, and grade.
        What it does is instantiates that student objects inside the method, via the parameters on line 25.
        These objects are then added to the dictionary, via a student_id key. However, if the student 
        object in question already exists, then this method will stop and print a message stating that 
        this student is already in the dictionary.
        
        Future plan to implementing this method is to use an input token that takes in multiple arguments
        in a single instance. Through a try and except block, we can parse these arguments prior to them 
        being used so it does not crash the program, when an error occurs. Through this input token, we can
        pass these through as this method's arguments to add students. 
        
        Args:
            student_id (int): Takes in the student_id as an argument 
            first_name (str): Takes in the first_name as an argument
            last_name (str): Takes in the last_name as an argument
            age (int): Takes in the age as an argument
            grade (str): Takes in the grade as an argument.
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
        """_summary_
        """
        if not self.classroom:
            print("The classroom is empty.")
        for students in self.classroom.values():
            print(students)
            
    
    def find_student(self, id_to_find: int):
        for keys in self.classroom:
            if id_to_find == keys:
                print(str(self.classroom[id_to_find]) + "was found in the classroom.")
                return
            print(f"Student {id_to_find} was not found in the classroom.") 
            
            
    def get_classroom(self):
        return self.classroom