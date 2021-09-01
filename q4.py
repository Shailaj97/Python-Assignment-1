#	Given a sentence use string split and join to get the result as shown below:
#Sample Input: this is a string
#Sample Output: this-is-a-string

a=input('Enter a sentence: ')
a=a.split(" ")     #Sentence needs to be split first else, join puts – before every letter
a="-".join(a)
print(a)
