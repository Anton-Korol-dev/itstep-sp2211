class Student:
    def __init__(self, name=None, height=170):
        self.name = name
        self.height = height

    def __bool__(self):
        return self.name != None
    
    def __len__(self):
        return self.height

nick = Student()
print(nick.__len__())
print(nick.__bool__())
print(len(nick))
print(bool(nick))

