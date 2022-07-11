from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    result = 0
    len_arr = len(temperatures)
    if len_arr == 1:
        return 1
    if temperatures[0] > temperatures[1]:
        result += 1
    for i in range(1, len_arr - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            result += 1
    if temperatures[len_arr - 1] > temperatures[len_arr - 2]:
        result += 1
    return result


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
