def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    # Старое решение:
    if index is None:
        return list_[0:-1]
    elif index >= 0: 
        return list_[0:index] + list_[index + 1:]
    else:
        return list_[0:index - 1] + list_[index:]

    # Решение со списочным выражением:
    # if index is None:
    #     index = len(list_) - 1
    # return [list_[i] for i in list_ if i != index]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
