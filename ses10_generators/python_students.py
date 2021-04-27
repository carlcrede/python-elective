
"""
Based on the Student class below, create a PythonStudents class 
that acts as a collection of students. The class should implement 
the iterations functionality (iter() and next()) and be able to 
return an iter object. When iterated the Pythod_students object 
should return the name of each student in the list.
"""


class PythonStudents:

    def __init__(self):
        self.students = []

    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        current_index = self.index
        self.index += 1
        if self.index > len(self.students):
            raise StopIteration()
        return self.students[current_index]

    def __add__(self, student):
        self.students.append(student)


class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'{self.__dict__}'