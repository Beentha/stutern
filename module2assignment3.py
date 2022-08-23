# Module 2, assignment 1

"""
Write a python program to generate and print 
a dictionary containing keys ranging from 5 to 15 
(with both numbers included) and the values are the squares of the keys.
"""

my_dict = dict()
for i in range(5, 16):
    my_dict[i] = i**2

print(my_dict)

