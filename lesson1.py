class Student:
    def __init__(self, name=None, height=170):
        self.name = name
        self.height = height

#     def __del__(self):
#         print(f"Student {self.name} is being deleted")

# Nick = Student("Nick")
# del Nick
    def __bool__(self):
        # return bool(self.name)
        return self.name != None
    
    def __len__(self):
        return self.height
    
Nick = Student("Nick")
print(Nick.__len__())
print(Nick.__bool__())
print(len(Nick))
print(bool(Nick))

