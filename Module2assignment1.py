# Module 2, assignment 1
"""
Define a function that returns the maximum 
of any three numbers a user inputs. 

Assign the result to a variable “max_num”
"""


def max_of_three(x, y, z):

    list_of_input = [x, y, z]
    max_num = max(list_of_input)
    return max_num


max_num = max_of_three(15, 17, 25)
print(max_num)
