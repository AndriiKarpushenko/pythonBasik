# Home work 8.2

import string


def is_palindrome(text):
    def clean_string(text):
        cleaned_string = ''.join(char for char in text if char.isalnum())
        return cleaned_string.lower()

    cleaned_string = clean_string(text)

    return cleaned_string == cleaned_string[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
