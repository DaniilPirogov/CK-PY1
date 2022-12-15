from random import randint


def get_unique_list_numbers(a=15, b=-10, c=10) -> list[int]:
    arr_ = []
    while len(set(arr_)) < a:
        arr_.append(randint(b, c))
    return list(set(arr_))
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
