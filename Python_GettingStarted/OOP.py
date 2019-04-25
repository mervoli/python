"""
 * Example of Object Oriented Programming in Python
 * Copyright (C) 2019 Merve KILINC YILDIRIM
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

#Class
student_list = []

"""
Base class
"""
class Student:
    school_name = "MyCollege"
    def __init__(self, name, id = 0):  #Constructor
        self.add_student(name, id)


    def __str__(self): #Tostr functions, overloaded
        return "Student: " + self.name + " School: " + Student.school_name


    def add_student(self, name, id = 0):  #self is the first parameter for memeber functions
        self.name = name
        self.id = id
        student = {"Name": name, "Id": id}
        student_list.append(student)

"""
This class is inherited from Student class
"""
class HighSchoolStudent(Student):
    school_name = "MyHighCollege"  #override class attr
    def __init__(self, name, id = 0):
        super().add_student(name, id)  #calls base class's function

    def __str__(self):
        return "High School Student: " + self.name + " School: " + HighSchoolStudent.school_name


my_student = Student("Elif")
print(my_student)
my_highschool_student = HighSchoolStudent("Merve")
print(my_highschool_student)
