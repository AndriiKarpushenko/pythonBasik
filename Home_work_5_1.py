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

        if input_string in keyword.kwlist:
            print(False)
        else:

            contains_underscore_letters = False
            index = 0
            while index < len(input_string) - 1:
                if input_string[index] == '_' and input_string[index + 1] == '_':
                    contains_underscore_letters = True
                    break
                elif input_string[index] == '_' and input_string[index + 1] != '_':
                    contains_underscore_letters = False
                    break
                index += 1

            if contains_underscore_letters:
                print(False)
            else:
                print(True)