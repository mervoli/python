"""
 * Example of Types, Statements and Other Things in Python
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

#Type casting
pi = 3.1415
int_pi = int(pi)
str_pi = str(pi)

print(int_pi, pi, str_pi) #prints 3 3.1415 3.1415

#Some string functions
str = "hello"
new_str = str.capitalize().replace('e', 'a')
print(str, new_str)

is_alpha = str.isalpha()
is_digit = str.isdigit()

#generates a list with members (apple, orange, kiwi, strawberry)
fruit_list = "apple, orange, kiwi, strawberry".split(',')

name = "merve"
age = 30
print("Hello {0}. Your age is {1}".format(name, age)) #format() function

#If statements
if(name == "merve" and age == 30):
    print("This is me :)")
else:
    print("This is not me :(")

#Lists
names = [] #empty list
student_names = ["Elif", "Berra", "Hira", "Azra"]

student_names.append("Bekir") #add new name to student_names
print(student_names[0])

student_num = len(student_names)

del(student_names[0])
print(student_names[0])

#Loops
for name in student_names:
    print(name)

for i in range(10): #print 1-9
    print(i)

while i>0:
    print(i)
    i = i-1
    if i==5:
        break

#Dictionaries
student_dict = {"Name": "Elif", "Age": 4, "Num": 100}
stdudents_list = [{"Name": "Berra", "Age": 4, "Num": 200},
                  {"Name": "Hira", "Age": 4, "Num": 300},
                  {"Name": "Azra", "Age": 4, "Num": 400}]

student_dict["School"] = "Kindergarden" #to add a new key-value pair
student_dict["Name"] = "Merve" #to change the value of the "Name"
name = student_dict["Name"] #to get the value of the "Name"

print(student_dict.keys())
print(student_dict.values())

#Exceptions
try:
    print(student_dict["City"])
except Exception: #This is the general exception type. Eg. KeyError, TypeError, ...
    print("A general exception occured.")

