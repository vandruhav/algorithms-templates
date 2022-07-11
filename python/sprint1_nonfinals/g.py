def to_binary(number: int) -> str:
    result = ''
    while number >= 2:
        result += str(number % 2)
        number //= 2
    if number == 1:
        result += str(number)
    return result[::-1]


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
