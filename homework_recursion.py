def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

entered_number = input('Введите число: ')
result = get_multiplied_digits(entered_number)
print(f'Произведение цифр числа {entered_number} равно {result}')