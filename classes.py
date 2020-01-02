class Student:
    students = []
    school_name = "My school" # static class variables

    def __init__(self, name, student_id=223): # constructor
        self.name = name
        self.student_id = student_id
        self.students.append(self)

    def __str__(self): #override
        return "Student " + self.name

    def get_name_cap(self):
        return self.name.capitalize()

    def get_sch(self):
        return self.school_name

student = Student('ritesh')
print(student)
print(student.school_name)
print(Student.school_name)