# -*- coding: utf-8 -*-

def get_list() -> list:
    t = True
    result = []
    print("Введите элементы по одному. Чтобы закончить ввод нажмите просто ENTER")
    while t:
        el = input()
        if el == "":
            return result
        result.append(el)


def sort_list(l: list) -> list:
    result = []
    for el in l:
        if len(el) < 4:
            result.append(el)
    return result


if __name__ == '__main__':
    strings_list = get_list()
    print("ввели: ", strings_list)

    result = sort_list(strings_list)
    print("получили:", result)
