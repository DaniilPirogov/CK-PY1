import string
from random import sample


digits = list(map(str, list(range(0, 10))))
letters = list(string.ascii_letters)


def get_random_password(a=8) -> str:
    population = digits + letters
    password = sample(population, a)
    return ''.join(password)
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
