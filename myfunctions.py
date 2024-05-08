

def prime_number2(number: int) -> bool:
    if number<2:
        prime = False
    limit = int(number/2) + 1
    for n in range(2, limit):
        if number % n == 0:
            prime = False
        else:
            prime = True
        print(n, prime)
    return prime

def prime_number(number: int) -> bool:
    if number <2:
        return False
    limit = int(number/2) + 1
    for n in range(2, limit):
        if number % n == 0:
            return False
    return True


def prime_number3(number: int) -> bool:
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
        



    # 222222222222222222222222