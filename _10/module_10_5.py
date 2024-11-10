import time
from datetime import timedelta
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
# for file in filenames:
#     read_info(file)
# print('Линейный ввызов занял: ', timedelta(seconds=time.time()-start_time))

if __name__ == '__main__':
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    print('Многопроцессный ввызов занял: ', timedelta(seconds=time.time() - start_time))