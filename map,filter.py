from collections import namedtuple
Circle = namedtuple('Circle',['radius'])
circle = Circle(10)

print(circle[0]) #10
print(circle.radius) #10