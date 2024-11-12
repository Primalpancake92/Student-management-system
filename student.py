class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, age: int, grade: str):
        """_summary_

        Args:
            student_id (int): _description_
            first_name (str): _description_
            last_name (str): _description_
            age (int): _description_
            grade (str): _description_
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
        formatted = self.first_name + " " + self.last_name
        return formatted
    
    
    def get_age(self) -> str:
        formatted = str(self.age)
        return formatted
    
    
    def get_grade(self) -> str:
        return self.grade
    
    
    def set_student_id(self, student_id: int):
        self.student_id = student_id
        
    
    def set_full_name(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        
    
    def set_age(self, age: int):
        self.age = age
    
    
    def set_grade(self, grade: str):
        self.grade = grade
        
