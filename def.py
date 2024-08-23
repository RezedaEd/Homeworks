def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        z = []
        for j in range(m+1):
            z.append([value] * j)
        matrix.append(z[j])
    return matrix


result_1 = get_matrix(6, 2, 9)
result_2 = get_matrix(4,3,1)
result_3 = get_matrix(2,4,55)
print(result_1, result_2, result_3, sep='\n')
