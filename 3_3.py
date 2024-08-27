def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('t')
print_params(6, 3)
print_params((6, 5), [3, 1], 'kk')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, 3, [1, 1]]
values_dict = {'a': 'cat', 'b': 4, 'c': (2,2)}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['time', (2, 3)]
print_params(*values_list_2, 42)