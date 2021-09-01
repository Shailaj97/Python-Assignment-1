"""	Write a Python program to get the following pattern using a nested loop.
1
22
333
4444
55555
666666
7777777
88888888
999999999
"""


for i in range(0,9):
    for j in range(0,i+1):
        print(i+1,end=" ")
#end is  used to put a space after the string instead of a new line
    print("\r")
