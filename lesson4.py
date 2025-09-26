# class Parent:
#     classmethods and attrs
# class Child(Parent):
#     classmethods and attrs

class Human:
    height = 170
class Student(Human):
    satiety = 0
class Worker(Human):
    satiety = 100

nick = Student()
ann = Worker()
print(nick.satiety)
print(ann.satiety)