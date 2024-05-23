def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()                           # вызов функции без аргументов
print_params('новая строка', 15)   # переопределила значение параметров 'a' и 'b'
print_params(3, c=False)              # переопределила значение, которое автоматически позиционно передастся параметру 'а', затем указала именованный параметр 'c'
print_params(b=25)                       # переопределила значение параметра 'b'
print_params(c=[1,2,3])                  # переопределила значение параметра 'c'


values_list = [[5, 7, 9], 888, 'Python']
values_dict = {'a': 'Привет', 'b': True, 'c': 500}

print_params(*values_list)     # распаковали список, и значения из списка встанут на место соответствующее каждому параметру функции (a, b, c)
print_params(**values_dict)    # распаковали словарь, и значения из словаря встанут на место соответствующее каждому параметру функции (a, b, c)


values_list_2 = [True, 'Отлично']
print_params(*values_list_2, 42)    # значение из распакованного списка переопределят значения параметров 'a' и 'b' соответственно. Затем переопределили значение параметра 'c'