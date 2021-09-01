"""	Map, Filter, Reduce Question:  Given a list of strings fruits as shown below:
 fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"].
a.	Change each of the words to uppercase using map function
b.	Filter out the words starting with ‘A’ using filter functionality
c.	Concat all words using reduce
"""

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
list(map(str.upper , fruits))
list(filter(lambda x: list(x)[0]=='A',fruits))
from functools import reduce
reduce(lambda x,y: x+y , fruits)
