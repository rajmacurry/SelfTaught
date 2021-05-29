class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self,student):
        if len(self.students) < self.max_students :
            self.students.append(student)
            return True
        else:
            print("Max number of students reached for this course")
            return False

    def get_average_grade(self):
        sum=0
        tot=len(self.students)
        for stud in self.students:
            sum += stud.get_grade()
        avg_grade = sum/tot
        return avg_grade

s1 = Student("Raj", 21, 86)
s2 = Student("Shreya",20, 85)
s3 = Student("Sumanta", 22, 75)
s4 = Student("Rabik", 22, 78)

course1 = Course("Python_course", 4)
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)
course1.add_student(s4)
print(course1.students)
print(course1.get_average_grade())