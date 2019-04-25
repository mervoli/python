"""
 * Example of Functions in Python
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

#Functions
fruit_list = "apple, orange, kiwi, strawberry".split(',')

def insert_fruit(fruit = "lemon"):
    fruit_list.append(fruit)


insert_fruit() #insert lemon when no value is given as a parameter
insert_fruit("banana")


def get_fruit():
    return fruit_list[0]


my_fruit = get_fruit()

#File Operations
my_file = open("temp.txt", "r") #File is opened in read mode.
file_content = my_file.readlines()
my_file.close()

for fruit in file_content:
    print(fruit)
