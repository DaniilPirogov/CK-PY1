from random import sample


digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
population = digits + lowercase_letters + uppercase_letters


def get_random_password() -> str:
    password = sample(population, 8)
    return ''.join(password)
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
