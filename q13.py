"""Write a Program to read a sample text file and count the words having length greater than or equal to 5."""
a=0
with open('sample.txt', 'r') as file:

    for i in file:


        for word in i.split():
            if len(word)>=5:
                a=a+1
print(" The no of words : " ,a)
