"""ID: 69363264"""
from typing import Any

house_numbers: Any = []
"""Список домов и пустых участков."""


def nearest_zero() -> None:
    """Возвращает список расстояний до ближайшего пустого участка."""
    global house_numbers
    len_street = len(house_numbers)
    prev_zero = -10000000
    """Индекс предыдущего пустого участка в списке house_numbers."""
    next_zero = -1
    """Индекс следующего пустого участка в списке house_numbers."""
    for i in range(len_street):
        if i > next_zero:
            next_zero = i
            while house_numbers[next_zero] != 0:
                next_zero += 1
                if next_zero == len_street:
                    next_zero = 10000000
                    break
        if house_numbers[i] == 0:
            prev_zero = i
        else:
            house_numbers[i] = min(i - prev_zero, next_zero - i)


def read_input() -> None:
    """Позволяет ввести длину улицы и список домов и пустых участков."""
    global house_numbers
    input()
    house_numbers = [int(number) for number in input().strip().split()]


if __name__ == '__main__':
    """Главный модуль."""
    read_input()
    nearest_zero()
    print(*house_numbers)
