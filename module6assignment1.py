integer_list = [num for num in range(int(5.5), int(20.5))]

# count even number
count_even_number = len(list(filter(lambda num: (num % 2 == 0), integer_list)))
print("count of even numbers: ", count_even_number)

# count odd number
count_odd_number = len(list(filter(lambda num: (num % 2 != 0), integer_list)))
print("count of odd numbers: ", count_odd_number)

# square every number in the list
square_list = list(map(lambda num: (num ** 2), integer_list))
print(square_list)

# cube every number in the list
cube_list = list(map(lambda num: (num ** 3), integer_list))
print(cube_list)