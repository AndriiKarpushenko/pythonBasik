# Home work 2.2

five_digit_number = input("Please enter a 5-digit number: ")
five_digit_number=int (five_digit_number)

first_digit=five_digit_number//10000
second_digit=(five_digit_number % 10000)//1000
third_digit=(five_digit_number % 1000)//100
fourth_digit=(five_digit_number % 100)//10
fifth_digit=(five_digit_number % 10)

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
print(fifth_digit)

# Отримуємо кожну цифру числа
# digit1 = number // 10000
# digit2 = (number % 10000) // 1000
# digit3 = (number % 1000) // 100
# digit4 = (number % 100) // 10
# digit5 = number % 10

