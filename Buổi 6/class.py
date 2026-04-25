# Class & Object
class Dog:
    species = "Canis familiaris"      # class attribute (chung cho mọi instance)

    def __init__(self, name, age):    # constructor
        self.name = name              # instance attribute
        self.age = age

    def bark(self):                   # method
        return f"{self.name} says Woof!"

dog1 = Dog("Rex", 3)                 # tạo object (instance)

# Access Modifier
class Person:
    def __init__(self):
        self.name = "Dat"       # public   — truy cập tự do
        self._age = 25          # protected — quy ước không dùng ngoài class
        self.__salary = 1000    # private   — không truy cập trực tiếp từ ngoài

