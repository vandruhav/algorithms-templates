def is_palindrome(line: str) -> bool:
    len_line = len(line)
    if len_line == 0:
        return False
    symbols = ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    start = 0
    end = len(line) - 1
    while end > start:
        if line[start] in symbols:
            start += 1
            continue
        if line[end] in symbols:
            end -= 1
            continue
        if line[start].lower() != line[end].lower():
            return False
        start += 1
        end -= 1
    return True


print(is_palindrome(input().strip()))
