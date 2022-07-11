def get_longest_word(line: str) -> str:
    result = ''
    max_len = 0
    arr = line.split(' ')
    for word in arr:
        if len(word) > max_len:
            max_len = len(word)
            result = word
    return result


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
