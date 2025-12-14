class Student:
    def __init__(self, name, number, GPA= 0.0):
        self.name = name
        self.number = number
        self.GPA = GPA

    def set_GPA(self, new_gpa):
        self.GPA = new_gpa

    def __str__(self):
        return f"Student(name={self.name}, number={self.number}, GPA= {self.GPA})"
