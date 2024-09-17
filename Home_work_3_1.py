# Home work 3.1

first_number = input("Please enter the first number: ")
first_number = float (first_number)

second_number = input("Please enter the second number: ")
second_number = float (second_number)

action = input("Select an action: (+, -, *, /) ")

if action == '+':
    calculation_result = first_number + second_number
elif action == '-':
    calculation_result = first_number - second_number
elif action == '*':
    calculation_result = first_number * second_number
elif action == '/':
    if second_number == 0:
        calculation_result = "Error: Division by zero!"
    else:
        calculation_result = first_number / second_number

print("Calculation result:", calculation_result)