def delete(list_, index=None):
    ...  # TODO реализовать функцию удаления элемента из списка по индексу
    if index is not None:
        return list_[0:index] + list_[index + 1:]
    else:
        return list_[0:-1]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
