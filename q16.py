"""	Map, Filter, Reduce Question:  Given a list of strings fruits as shown below:
 fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"].
a.	Change each of the words to uppercase using map function
b.	Filter out the words starting with ‘A’ using filter functionality
c.	Concat all words using reduce
"""

from functools import reduce
fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
print(list(map(str.upper , fruits)))
print(list(filter(lambda x: list(x)[0]=='A',fruits)))


print(reduce(lambda x,y: x+y , fruits))
