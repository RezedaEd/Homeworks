def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result_1 = get_multiplied_digits(40203)
result_2 = get_multiplied_digits(512)
result_3 = get_multiplied_digits(2)
print(result_1, result_2, result_3, sep='\n')