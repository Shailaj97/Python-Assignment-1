"""	Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""


for i in range(1):
    for j in range(1,10):
        if j<=5:
            print('*'*j)
        else:
            print('*'*(10-j))
