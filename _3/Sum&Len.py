def calculate_structure_sum(*a):
    res = 0
    for i in a:
        if isinstance(i, str):
            res = res + len(i)
        elif isinstance(i, int):
            res = res + i
        elif isinstance(i, (list, tuple, set)):
            res = res + calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                res = res + len(key) + value
    return res


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)