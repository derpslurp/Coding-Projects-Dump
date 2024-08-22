#Namedtuple only makes the access more convenient, by using names instead of indices
from collections import namedtuple

Point = namedtuple('Point', 'x y z')

newP = Point(3,4,5)
print(newP)