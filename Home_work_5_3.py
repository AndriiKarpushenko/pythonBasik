# Home work 5.3

import string

user_string = input("Input user string: ")

user_string = user_string.title()

string_without_spaces_and_punctuation = ""
for char in user_string:
    if char not in string.punctuation and char != " ":
        string_without_spaces_and_punctuation += char

string_with_hashtag = "#" + string_without_spaces_and_punctuation

if len(string_with_hashtag) > 140:
    string_with_hashtag = string_with_hashtag[:140]

print(string_with_hashtag)