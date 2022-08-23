import numpy as np

arr = np.arange(1, 101)
lcm_of_even_numbers = np.lcm.reduce(list(filter(lambda num : (num % 2 == 0), arr)))
print(lcm_of_even_numbers)
