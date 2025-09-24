class Student:
    amount_of_students = 0
    def __init__(self, height = 170):
        self.height = height
        Student.amount_of_students += 1
    def grow(self, height):
        self.height += height

Ira = Student()
print("Ira height before growing: ", Ira.height)
Andriy = Student(height=180)
Ira.grow(height=5)
print("Ira height after growing: ", Ira.height)
print(Andriy.height)