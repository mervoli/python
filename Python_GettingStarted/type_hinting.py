"""
 * Example of Type Hinting in Python
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
print("Type Hinting")

def add_number(a, b):
    return a+b


def add_number2(a: int, b: int):
    return a+b


sum1 = add_number(2.58, 3.54)
sum2 = add_number2(2.58, 3.54)

print("sum1: {0}\nsum2: {1}".format(sum1, sum2))

