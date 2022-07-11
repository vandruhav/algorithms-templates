from math import sqrt
from typing import List


def factorize(number: int) -> List[int]:
    result = []
    sqrt_n = int(sqrt(number))
    num = number
    while num > 1:
        for i in range(2, sqrt_n + 1):
            if num % i == 0:
                result.append(i)
                break
        else:
            result.append(num)
            break
        num //= i
    return result


result = factorize(int(input()))
print(" ".join(map(str, result)))
