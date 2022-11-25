def xml_to_dict(file: str) -> dict:
    clean_file = file.replace('<?xml version="1.0"?>', '').replace('\n', '')
    result = {}
    index = 0

    while index < len(clean_file):
        opening_tag, start = get_tag(clean_file, index)
        closing_tag, end = get_closing_tag(clean_file, opening_tag, start)

        content = get_content(clean_file, start, end - len(closing_tag) - 2)

        result[opening_tag] = content

        index = end + 1

    return result


def get_content(file: str, start: int, end: int) -> tuple[str]:
    content = ''

    while start != end:
        content += file[start]
        start += 1

    return content


def get_closing_tag(content: str, opening_tag: str, index: int) -> tuple[str, int]:
    tag = ""
    while f'/{opening_tag}' != tag:
        tag, index = get_tag(content, index+1)

    return tag, index


def get_tag(content: str, index: int) -> tuple[str, int]:
    tag = ""
    nextIndex = index

    while index < len(content):
        car = content[index]
        if car == '<':
            index += 1
            continue
        if car == '>':
            nextIndex = index
            break

        tag += car
        index += 1

    return tag, nextIndex
