class Student:
    def __init__(self, name, number, courses=None):
        self.name = name
        self.number = number
        self.courses = courses if courses is not None else []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        course_list = [course.title for course in self.courses]
        return f"Student(name={self.name}, number={self.number}, courses={course_list})"
