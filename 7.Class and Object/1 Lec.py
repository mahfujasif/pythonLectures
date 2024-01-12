

# class Point:
#     def __init__(self, inX, inY):
#         self.x = inX
#         self.y = inY
#     def setLocation(self, newX, newY):
#         self.x = newX
#         self.y = newY
#
#
# p1 = Point(1,2)
# print(p1.x, ":", p1.y)
# p1.setLocation(20,30)
# print(p1.x, ":", p1.y)
# p1.x = 500
# p1.y = 600
# print(p1.x, ":", p1.y)


# class Point:
#     total = 0
#
#     def __init__(self, inX, inY):
#         self.x = inX
#         self.y = inY
#         Point.total += 1
#
# p = Point(1,2)
# p = Point(3,4)
# print(p.total)
# p.total += 1
# print(p.total)


# class Point:
#     total = 0
#
#     def __init__(self, inX, inY):
#         self.x = inX
#         self.y = inY
#         Point.total += 1
#     @staticmethod
#     def status():
#         print("total:", Point.total)
#
# p = Point(1,2)
# p = Point(3,4)
# p.total += 1
# p.status()


#
# class Point:
#     def __init__(self):
#         self.__x = 0
#         self.__y = 0
#
#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y
#
#     def setX(self, x):
#         self.__x = x
#     def setY(self, y):
#         self.__y = y
#
#
# p = Point()
# print(p.getX(), ":", p.getY())
# p.setX(33)
# p.setY(35)
# print(p.getX(), ":", p.getY())


