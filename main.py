from student import Student
from course import Course
from data import students, courses

print("Welcome to Student Courses System")

student_objects = [Student(name, number) for name, number in students]
course_objects = [Course(code, title) for code, title in courses]

print("Students:")
for s in student_objects:
    print(" -", s)

print("\nCourses:")
for c in course_objects:
    print(" -", c)
