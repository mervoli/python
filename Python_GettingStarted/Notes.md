## 1) Introduction

PEP (Python Enhancement Proposals). eg. PEP8: 2 blank lines before func def.
Installing python. To check enter: python --version
Installing Pycharm

## 2) Types Statements and Other Goodies

Dynamically typed. You don't have to declare variable.
But, you can use type hinting:

```
def add_number(a, b):
def add_number2(a: int, b: int):
```

### Type casting

`pi = 3.1415`
`int_pi = int(pi)`
`str_pi = str(pi)`

### Some string functions

`replace('a', 'b')`
`capitalize()`
`is_alpha()`
`is_digit()`
`split(',')`

### If statements

```
if a==b:
 ...
else:
 ...

if a!=b:
 ...
else:
 ...

if a==1 and b== 2:
 ...

if a!=0 or my_str:
 ...
```



### Lists

```
names = [] #empty list
student_names = ["Elif", "Berra", "Hira", "Azra"]
.append()
len()
zero index
del(student_names[0])
```



### Loops

`for name in student_names:`
`for i in range(10)`

```
while i>0:
break and continue statements
```


Note: No -- or ++ operands

### Dictionaries

key and value pairs
keys() and values() functions

### Exceptions

try and except blocks

```
try:

print(my_dict["key"])

except Exception:
```



### Other Types
- complex, long, 
- bytes, bytearray
- tuple
- set

## 3) Functions
### Functions
You can define a default value for a function parameter
`def insert_element(a = 0):`

### Nested Functions

Defining a function inside another function. Inner function can access the variables in outer function.

### File Operations

```
f = open("my_file.txt", "r") # open in read mode

f.write()

f.close()

f.readlines()
```

##### Access Modes

- "w": write
- "r": read
- "a": append
- "rb": read binary
- "wb": write binary

### Lambda Functions

## 4) Object Oriented Programming - Classes

### A Class

As a rule, naming for a function is all the letters are written in lowercase. And for class names, they begin with uppercase.

**Eg**. `class Student:`

**pass**:  if there is no definition for a class

And an object can be created by calling constructor

```
my_student = Student("Elif")
```

### Constructor

```
def __init__(self, name, id):
```

self is the first parameter for class functions.

### To str function

```
def __str__(self):
```

This function is overloadedto print out an object for the class.

### Class Attributes and Object Attributes

```
class Student:
	school_name = "MyCollege" #class atr
    def __init__(self, name, id): #Constructor
        self.add_student(name, id)

    def add_student(self, name, id = 0): 
        self.name = name # object attr
        self.id = id # object atrr
        student = {"Name": name, "Id": id}
```

Class attribute belongs to the class and object attribute belongs the the object.

### Inheritance

Inherits the base class

```
class HighSchoolStudent(Student):
```

With `super().base_function()`, calls the base class' function.

Can override the base class's function.

```
class HighSchoolStudent(Student):
    school_name = "MyHighCollege" #override class attr
    def __init__(self, name, id = 0):
        super().add_student(name, id) #calls base class's function

    def __str__(self):
        return "High School Student: " + self.name + " School: " + HighSchoolStudent.school_name
```

### Breaking into Modules

Every new class can be defined in a new file. When using this class, the module that is defined in this file must be imported.

Eg. If HighSchoolStudent class is defined in hs_student.py. You must import it as:

```
from hs_student import HighSchoolStudent
```

### Comments

Comments starts with # (for one line) and 

```
"""

Multiline comment

"""
```

**As a rule:** You should leave two spaces if the comment is in the same line with the code. And you should leave a breakline if comment is in a seperate line.

## 5) Python Tips and Tricks

### Virtual Environment

To create a virtual environment, First install **virtualenv**

- To create virtual environment:

  ```
  virtualenv my_virtualenv --python=python2.7
  ```

  this will create a virtual environment with name my_virtualenv  with python version python2.7

- To use:

  ```
  source path_to_my_virtualenv /bin/activate
  ```

- To leave:

  ```
  deactivate
  ```

### Creating Executables and Creating Setup

To create an .exe file, First install pyinstaller

- To create .exe file

  ```
  pyinstaller --onefile main.py 
  ```

To create a setup file, First install Inno Setup. Then a wizard can be used to create a setup file by using .exe file.

