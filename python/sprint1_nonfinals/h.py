from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    result = ''
    max_len = max(len(first_number), len(second_number))
    first_end = len(first_number) - 1
    second_end = len(second_number) - 1
    v_ume = 0
    for i in range(0, max_len):
        summa = ((int(first_number[first_end]) if first_end >= 0 else 0)
                 + (int(second_number[second_end]) if second_end >= 0 else 0)
                 + v_ume)
        if summa > 1:
            summa -= 2
            v_ume = 1
        else:
            v_ume = 0
        result = str(summa) + result
        first_end -= 1
        second_end -= 1
    if v_ume == 1:
        result = str(v_ume) + result
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
