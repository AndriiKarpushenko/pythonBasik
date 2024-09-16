# Home work 2.2

five_digit_number = input("Please enter a 5-digit number: ")
five_digit_number=int (five_digit_number)

first_digit=five_digit_number//10000
second_digit=(five_digit_number % 10000)//1000
third_digit=(five_digit_number % 1000)//100
fourth_digit=(five_digit_number % 100)//10
fifth_digit=(five_digit_number % 10)

first_digit_turn=fifth_digit*10000
second_digit_turn=fourth_digit*1000
third_digit_turn=third_digit*100
fourth_digit_turn=second_digit*10
fifth_digit_turn=first_digit

five_digit_number_turn = first_digit_turn + second_digit_turn + third_digit_turn + fourth_digit_turn + fifth_digit_turn

print(five_digit_number)
print('-----')
print(five_digit_number_turn)