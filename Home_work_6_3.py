# home_work_6_3

number_input = input("Введіть число: ")

product_numbers = 1
for num_digit in str(number_input):
    product_numbers *= int(num_digit)

while product_numbers > 9:
    temp_product_numbers = 1
    for num_digit in str(product_numbers):
        temp_product_numbers *= int(num_digit)
    product_numbers = temp_product_numbers

print("Результат обчислення:", product_numbers)
