from collections import Counter, namedtuple, deque
from operator import itemgetter
import random

fruits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']

# Using Counter to count occurrences of each fruit

fruit_counter = Counter(fruits)
print("\nFruit counts:", fruit_counter, "\n")   

# Using namedtuple to create a simple class for a Point
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)  
p2 = Point(30, 40)
print("Point 1:", p1)
print("Point 2:", p2)   

# Ordenar dictionaries por valor usando itemgetter
data = {'apple': 3, 'banana': 2, 'orange': 5}
sorted_data = sorted(data.items(), key=itemgetter(0))   
print("Sorted data by value:", sorted_data)   

# Utilizando uma final em ambas extremidades
dq = deque(['a', 'b', 'c'])
dq.append('d')  
dq.appendleft('z')  
print("Deque after appends:", dq, "\n")
dq.pop()  
dq.popleft()    
print("Deque after pops:", dq, "\n")


print(random.choice(fruits))




print()