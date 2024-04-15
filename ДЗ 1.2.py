class Person:
    def __init__(self, the_fullname, the_age, is_married):
        self.fullname = the_fullname
        self.age = the_age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Fullname: {self.fullname} the_age: {self.age} Married: {self.is_married}")
class Student(Person):
    def __init__(self, the_fullname, the_age, is_married, marks):
        super().__init__(the_fullname, the_age, is_married)
        self.marks = marks

class Teacher(Person):
    def __init__(self, the_fullname, the_age, is_married, experience, base_salary):
        super().__init__(the_fullname, the_age, is_married)
        self.experience = experience
        self.base_salary = base_salary

def create_students():
        student1 = Student("Baiel", 17, False, False)
        student2 = Student("Kanat", 17, False, False)
        student3 = Student("Bekemir", 18, False, False)
        return [student1, student2, student3]

students = create_students()

for student in students:
    student.introduce_myself()
    print("Silva:", student.marks)
    print()

teacher = Teacher ("Mr. Morgan", 47, True, 20, 40000)
teacher.introduce_myself()
print("Experience:", teacher.experience)
print("Base Salary:", teacher.base_salary)









