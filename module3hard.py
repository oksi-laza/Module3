data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


sum_ = 0
def calculate_structure_sum(*args):
    global sum_
    for params in args:
        if isinstance(params, list) == True or isinstance(params, tuple) == True or isinstance(params, set) == True:
            for value in params:
                # print(value)
                if isinstance(value, str) == True:    # если в списке, кортеже или множестве элементами являются строки
                    sum_ += len(value)
                elif isinstance(value, int) == True:  # если в списке, кортеже или множестве элементами являются числа
                    sum_ += value
                else:                                 # если что-то другое, то снова вызываем функцию, в которую положим этот элемент (список, кортеж, множества)
                    calculate_structure_sum(value)    # вызванная функция проверит элемент (список или кортеж или множество), прогнав снова по циклу и взяв каждый элемент, что там будет внутри списка - еще один кортеж или словарь и т.д или же сложит уже раскрытые значения или длину строки
        elif isinstance(params, dict) == True:        # если словарь, то преобразую в список, в качестве элементов списка будут и ключи, и значения
            converted_dict = []
            for i in params:
                converted_dict.append(i)
                converted_dict.append(params[i])
            calculate_structure_sum(converted_dict)   # получившийся из словаря список укажем в качестве параметра для вызываемой самой себя функции
        elif isinstance(params, str) == True:         # если параметр кортежа при очередном вызове функции равен 'str'
            sum_ += len(params)
        else:                                         # если параметр кортежа при очередном вызове функции 'int' или 'float'
            sum_ += params
    return sum_


result = calculate_structure_sum(data_structure)
print(result)


