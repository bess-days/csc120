class Student:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    def get_name(self):
        return self._name
    def get_id(self):
        return self._id

student = Student("Harry", 987)
class Counter:
    def __init__(self, name):
        self._name = name
        self._count = 0
        self._number = 0
    def click(self):
        self._count += 1
    def count(self):
        return  print('Results for' + str(self._name) + ":" + str(self._count))
    def reset(self):
        self._count = 0
        self._number += 1
    def reset_count(self):
        return self._number

import math
class Point:
    def __init__(self, x, y):
     self._x = x
     self._y = y
    def translate(self, dx, dy):
        self._x += dx
        self._y += dy
    def distance_from_origin(self,x, y):
        return math.dist([0,0], [x,y])