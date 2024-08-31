first_num = int(input("Введите число от 3 до 20: "))
password = []
if 3 <= first_num <= 20:
    for i in range(1, first_num // 2 + 1):
        for j in range(i + 1, first_num):
            sum = i + j
            if first_num % sum == 0:
                password.append(i)
                password.append(j)
            else:
                continue
    print(*password, sep='')
else:
    print ('Введено число не принадлежащее диапазону. Попробуйте снова.')