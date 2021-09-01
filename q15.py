#	Write a function in Python that takes a normal .txt file path as an input and counts the word in a given list [ the, these, that, and]  and displays it.

with open('sample.txt', 'r') as my_file:
    c = 0

    while True:
        a = my_file.readline()

        if not a: break

        words = a.split()

        for i in words:
            if i.lower() in ('the', 'this', 'that', 'and'): c += 1
    print(c)
