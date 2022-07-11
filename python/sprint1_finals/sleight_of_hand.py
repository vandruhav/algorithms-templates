"""ID: 69363291"""
from typing import Tuple


def sleight_of_hand(input_data: Tuple[int, str]) -> int:
    """Возвращает максимальное количество баллов для двух игроков."""
    result = 0
    num_keys = input_data[0] + input_data[0]
    for i in '123456789':
        result += 1 if 0 < input_data[1].count(i) <= num_keys else 0
    return result


def read_input() -> Tuple[int, str]:
    """
    Позволяет ввести кол-во клавиш, нажатых одним игроком, и поле тренажёра.
    """
    k = int(input())
    symbols = ''
    for _ in range(4):
        symbols += input().strip()
    return k, symbols


if __name__ == '__main__':
    """Главный модуль."""
    print(sleight_of_hand(read_input()))
