# class Parent:
#     classmethods and attrs
# class Child(Parent):
#     classmethods and attrs

# class Human:
#     height = 170
#     satiety = 50
# class Student(Human):
#     satiety = 0
# class Worker(Human):
#     satiety = 100

# nick = Student()
# ann = Worker()
# print(nick.satiety)
# print(ann.satiety)

class Grandparent:
    height = 170
    satiety = 100
    age = 60
class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
nick = Child()