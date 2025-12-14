class Teacher:
    def __init__(self, name, number):
        self.name = name
        self.phone_number = number


    def __str__(self):
        return f"Student(name={self.name}, phone_number={self.number})"
