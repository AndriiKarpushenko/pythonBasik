# Home work 5.1

import string
import keyword

input_string = input("input string: ")

if input_string[0].isdigit():
    print(False)
else:
    search_capital_letters = False
    for letter in input_string:
        if letter.isupper():
            search_capital_letters = True
            break

    search_space = False
    for letter in input_string:
        if letter.isspace():
            search_space = True
            break

    search_punctuation = False
    for letter in input_string:
        if letter in string.punctuation.replace('_', ''):
            search_punctuation = True
            break

    if search_capital_letters or search_space or search_punctuation:
        print(False)
    else:

        if input_string.count('_') > 1:
            print(False)
        else:

            if input_string in keyword.kwlist:
                print(False)
            else:
                print(True)
