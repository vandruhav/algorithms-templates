from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    short = list(shorter)
    long = list(longer)
    for i in short:
        if i in long:
            long.remove(i)
    result = ''.join(long)
    return result


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
