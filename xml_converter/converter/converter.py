def xml_to_dict(file: str) -> dict:
    clean_file = file.replace(
        '<?xml version="1.0"?>',
        '',
    ).replace('\n', '').strip()
    result = {}
    index = 0

    while index < len(clean_file):
        opening_tag, start, end, content = convertNode(
            clean_file, index,
        )

        tag, _ = get_tag(content, 0)
        has_no_sub_tag = tag == ""
        if has_no_sub_tag:
            result[opening_tag] = content
            index = end + 1
            continue

        startIndex = start + 1
        endIndex = end - len(opening_tag) - 2

        slice = clean_file[startIndex:endIndex]

        sub_tags = xml_to_dict(slice)
        result[opening_tag] = [{key: sub_tags[key]} for key in sub_tags]

        index = end + 1

    return result


def convertNode(clean_file, index):
    opening_tag, start = get_tag(clean_file, index)
    closing_tag, end = get_closing_tag(clean_file, opening_tag, start)

    content = get_content(clean_file, start+1, end - len(closing_tag) - 1)

    return opening_tag, start, end, content


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
    tagStarted = False

    while index < len(content):
        car = content[index]
        if car == '>':
            nextIndex = index
            break
        index += 1

        if car == '<':
            tagStarted = True
            continue

        if not tagStarted:
            continue

        tag += car

    return tag, nextIndex
