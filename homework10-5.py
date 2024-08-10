import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, encoding='utf-8') as file:
        data = file.readline()
        while data:
            all_data.append(data.strip())
            data = file.readline()


all_files = [f"./files/file {i}.txt" for i in range(1, 5)]

# start = datetime.now()
# for file in all_files:
#     read_info(file)
# end = datetime.now()
# print(end - start)


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, all_files)
    end = datetime.now()
    print(end - start)

# 0:00:06.622352  - Линейный метод
# 0:00:02.361147  - Многопроцессорный метод