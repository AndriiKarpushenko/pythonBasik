# Home work 4.2

import random

random_number_elements = random.randint(3, 10)

random_list = [random.randint(1, 100) for i in range(random_number_elements)]

new_random_list = [random_list [0], random_list [2], random_list [-2]]

print(random_number_elements)
print(random_list)
print(new_random_list)