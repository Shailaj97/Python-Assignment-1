#Write a Python program to get the smallest and largest number from a list of integers.


a=[]
b=int(input("Enter the number of elements you want in the list :"))
for i in range(b):
        c=int(input("Enter a number:"))
        #Take values in a new variable and append it into the empty list a
        a.append(c)
print(a)
print("The largest element is :", max(a))
print("The smallest element is:" , min(a))
