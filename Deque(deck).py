#A deque is a double-ended queue in which elements can be both inserted and deleted from either the left or the right end of the queue
from collections import deque

d = deque('hello')
d.append('4')
d.popleft()
print(d)
