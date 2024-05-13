import random

# 1. VER SI UN NÚMERO ES PRIMO O NO


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


# 2. GENERAR PASSWORD ALEATORIO

"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 """

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "¿", "?", "(", ")", "/", "&", "%", "$", "!", "<", ">"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def generate_password(leng: int) -> str:
    if leng >= 8 and leng <= 16:
        random_characters = random.choices(characters, k=leng)
        str_num = [str(i) for i in numbers]
        random_num = random.choices(str_num, k=leng)
        psw = random_characters + random_num
        # print("psw 1", psw)
        psw = random.choices(psw, k=leng)
        # random.shuffle(psw)
        # print("psw 2", psw)
        concat_psw = "".join(psw)
        # le = len(concat_psw)
        # print("Su password es => ", concat_psw)
        # print("Su password es de longitud => ", le)
        return concat_psw
    else:
        raise ValueError("Longitud del password debe estar entre 8 y 16")

# 3. PASAR NÚMERO DECIMAL A BINARIO


def decimal_to_binary(decimal: int) -> int:
    rest = []
    while decimal > 0:
        rest.append(decimal % 2)
        decimal = int(decimal/2)
        print("resto", rest)
        print("nuevo decimal", decimal)
    rest.reverse()
    str_rest = [str(i) for i in rest]
    concat_rest = "".join(str_rest)
    return concat_rest


print("binary", decimal_to_binary(10))
print("binary", decimal_to_binary(15))
