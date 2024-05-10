def prime_number(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Should send a integer")
    if number < 2:
        return False
    limit = int(number/2) + 1
    for n in range(2, limit):
        if number % n == 0:
            return False
    return True


def prime_number_v0(number: int) -> bool:
    if not isinstance(number, int):
        raise TypeError("Should send a integer")
    result = True
    if number < 2:
        result = False
    else:
        limit = int(number/2) + 1
        for n in range(2, limit):
            if number % n == 0:
                result = False
                break
    return result
