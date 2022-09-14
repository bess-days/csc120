"""1.
a.init()
b. name
c. objects
"""

class Counter:
    def __init__(self, name):
        self._name = name
        self._count = 0
    def click(self):
        self._count += 1
    def my_conter(self):
        print(self._name, self._count)
    def count(self):
        return self._count


object = Counter("bob")
object.click()
print(object.count())
object.my_conter()
object.my_conter()
"""It prints 0, or prints class_xxxx"""

"""print('Results for' + str(self._name) + ":" + str(self._count))"""

import math
class Point:
    def __init__(self, x, y):
     self._x = x
     self._y = y
    def translate(self, dx, dy):
        self._x += dx
        self._y += dy
    def distance_from_origin(self,x, y):
        return math.sqrt( ((x[0]-y[0])**2)+((x[1]-y[1])**2) )


"""
You can impend for i in range len(number of clicks) -1
"""


