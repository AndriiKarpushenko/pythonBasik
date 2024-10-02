# Home work 9.1._rev

import string


def popular_words(text, words):
    text = text.lower().split()
    dictionary_for_results = {}

    for word in words:
        dictionary_for_results[word] = text.count(word)

    return dictionary_for_results


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
