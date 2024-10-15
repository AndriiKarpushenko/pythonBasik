# Home Work 12.1

import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()

    cleaned_content = html_content

    while '<' in cleaned_content and '>' in cleaned_content:
        start = cleaned_content.find('<')
        end = cleaned_content.find('>') + 1
        cleaned_content = cleaned_content.replace(cleaned_content[start:end], '')

    non_empty_lines = []
    for line in cleaned_content.split('\n'):
        if line.strip():
            non_empty_lines.append(line)
    cleaned_content = '\n'.join(non_empty_lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_content)


delete_html_tags('draft.html')
