"""	Write a Python program to find the key of the maximum value in a dictionary.
Sample Output:
Original dictionary elements
{'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
the maximum and minimum value of the said dictionary:
('Roxanne', 'Theodore')
"""

a={
    'Theodore': -19,
    'Roxanne': -22,
    'Mathew': -21,
    'Betty': -20
}

b=max(a, key= lambda x: a[x])
c=min(a, key= lambda x: a[x])
print(b)
print(c)
