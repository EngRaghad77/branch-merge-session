class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number


    def __str__(self):
        return f"Student(name={self.name}, number={self.number})"
