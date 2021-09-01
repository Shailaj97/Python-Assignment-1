
"""Write a Python program to remove consecutive duplicates from a list.
Original list:
initial_input = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
final_output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
def duplicates(List):
    i = 0
    while i < len(List):
        if List[i] == List[i - 1]:
            del List[i]
        else:
            i += 1
    return List
list1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]


print('Filtered List : ', duplicates(list1))
