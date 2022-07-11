def is_power_of_four(number: int) -> bool:
    i = 0
    result = 0
    while result < number:
        result = 4 ** i
        if result == number:
            return True
        i += 1
    return False


print(is_power_of_four(int(input())))
