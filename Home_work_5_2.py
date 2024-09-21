# Home work 5.2

while True:

    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))


    # Запитуємо у користувача дію, яку він хоче виконати
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
    else:
        calculation_result = "Invalid action!"

    print("Calculation result:", calculation_result)


    continue_calculation = input("Do you want to perform another calculation? (yes/y to continue): ").lower()

    if continue_calculation not in ("yes", "y") :
        print("Calculations are over")
        break
