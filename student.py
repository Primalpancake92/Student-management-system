class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, age: int, grade: str):
        """This class stores the blueprint of every student object that is going to be added
        in the StudentManagementSystem dictionary. 

        Args:
            student_id (int): Takes in an integer as the student_id.
            first_name (str): Takes a string that is going to be the first name.
            last_name (str): Takes a string that is going to be the last name.
            age (int): Takes in an integer that is going to be the age of the object.
            grade (str): Takes in a character that is going to be the grade.
        """
        self.student_id = student_id 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.enrolled = False
        self.subjects_enrolled = {}
        
    
    def get_student_id(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        formatted = str(self.student_id)
        return formatted
    
    
    def get_name(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        formatted = self.first_name + " " + self.last_name
        return formatted
    
    
    def get_age(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        formatted = str(self.age)
        return formatted
    
    
    def get_grade(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return self.grade
    
    
    def get_enrolment(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.enrolled
    
    
    def set_student_id(self, student_id: int):
        """_summary_

        Args:
            student_id (int): _description_
        """
        self.student_id = student_id
        
    
    def set_first_name(self, first_name: str):
        self.first_name = first_name
        
        
    def set_last_name(self, last_name: str):
        self.last_name = last_name
        
    
    def set_age(self, age: int):
        """_summary_

        Args:
            age (int): _description_
        """
        self.age = age
    
    
    def set_grade(self, grade: str):
        """_summary_

        Args:
            grade (str): _description_
        """
        self.grade = grade
        

    def set_enrolment(self, enrolment: bool):
        """_summary_

        Args:
            enrolment (bool): _description_
        """
        self.enrolled = enrolment
        
        
    def __str__(self):
        """_summary_
        """
        return f"\nStudent ID: {self.student_id}\nStudent Name: {self.first_name} + ' ' + {self.last_name}\nAge: {self.age}\nGrade: {self.grade}\nEnrolment Status: {self.enrolled}"