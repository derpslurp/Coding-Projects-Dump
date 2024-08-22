#Subclass of dict that's specially designed for counting hashable objects in Python
from collections import Counter


c = Counter('ching')
print(c)
c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)
c = Counter({'a':1, 'b':2})
print(c)
c = Counter(cats=4, dogs=7)
print(c['sd'])
