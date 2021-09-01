"""Write a Program to count the number of vowels in a given string.
	Example:
	Input_string = ‘Hello World’
	Count_output = 3"""

a = input("Enter a string: ")
b = 0
for i in a:
    if i in "aeiouAEIOU":
        b = b + 1
print("The number of Vowels: ")
print(b)
