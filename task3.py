from random import randint


def get_unique_list_numbers() -> list[int]:
    arr_ = []
    while len(set(arr_)) < 15:
        arr_.append(randint(-10, 10))
    return list(set(arr_))
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
