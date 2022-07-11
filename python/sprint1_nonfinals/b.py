def check_parity(a: int, b: int, c: int) -> bool:
    parity = a % 2
    if b % 2 != parity or c % 2 != parity:
        return False
    return True


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
