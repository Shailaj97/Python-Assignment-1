"""Write a Python program that prints all the numbers from 0 to 20
 except the numbers in the given list [ 5, 6, 12, 15].
Note : use the ‘continue' statement."""

for i in range(0, 21):
    if i in [5, 6, 12, 15]:
        continue
    else:
        print(i)

