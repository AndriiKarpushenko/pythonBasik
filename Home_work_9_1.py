# Home work 9.1

import string


def popular_words(text, words):
    text = text.lower()
    dictionary_for_results = {}

    for word_count in words:
        dictionary_for_results[word_count] = 0

    text_words = text.split()
    punctuation = set(string.punctuation)

    for word_count in text_words:
        if word_count in dictionary_for_results:
            dictionary_for_results[word_count] += 1

    return dictionary_for_results


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
