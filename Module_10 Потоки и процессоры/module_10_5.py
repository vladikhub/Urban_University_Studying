import time
from multiprocessing import Pool

#19.4
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        s = f.readline()
        while s:
            all_data.append(s.strip())
            s = f.readline()


file_names = [f'Files\\file {i}.txt' for i in range(1, 5)]
#
# start = time.time()
# for file in file_names:
#     read_info(f'Files\\{file}')
# end = time.time()
# print(start - end)

if __name__ == '__main__':
    start = time.time()
    pool = Pool()
    pool.map(read_info, file_names)
    end = time.time()
    print(end - start)
    