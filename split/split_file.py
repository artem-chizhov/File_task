
def count_(filename):
    with open(filename) as f:
        sum_ = sum(1 for _ in f)
    return sum_

list_file = ['1.txt','2.txt','3.txt']
list_file.sort()
with open('result.txt','w', encoding='utf-8') as f:
    for file_ in list_file:
        s = open((file_),encoding='utf-8').read()
        f.write(f"Имя файла {os.path.basename(file_)}\n")
        f.write(f"Количество строк в файле {str(count_(file_))}:\n")
        f.write(f"{s}\n")
