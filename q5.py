#	Write a Python program to find the difference between consecutive numbers in a given list.
#Original list: [4, 5, 8, 9, 6, 10]
#Difference between consecutive numbers of the said list: [1, 3, 1, -3, 4]



a=[4,5,8,9,6,10]
b=len(a)-1      #to avoid out of range error
c=[ ]
for i in range(b):
    diff=(a[i+1]-a[i])
    c.append(diff)
print(c)
