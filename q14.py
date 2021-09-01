#Write a program to read a sample text file and Capitalize the each word and append it to the same file.

with open('sample.txt', 'r') as a:
    for i in a:
        b = i.title()
        print(b)
