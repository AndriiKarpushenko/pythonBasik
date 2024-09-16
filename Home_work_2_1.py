# Home work 2.1

four_digit_number = input("Please enter a 4-digit number: ")

four_digit_number=int (four_digit_number)
first_digit=four_digit_number//1000
second_digit=(four_digit_number % 1000)//100
third_digit=(four_digit_number % 100)//10
fourth_digit=(four_digit_number % 10)

print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
