from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.__age = age   # Encapsulation

    @abstractmethod
    def display(self):
        pass

    def get_age(self):
        return self.__age


class Student(Person):

    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display(self):
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)


class Faculty(Person):

    def display(self):
        print("Faculty Name:", self.name)


student = Student("Abhishek", 22, 101)
faculty = Faculty("Vivek", 47)

student.display()
faculty.display()