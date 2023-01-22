#Работает, возвращает количество строк
len_list = []
def read_and_count(file_name):
    with open(file_name) as f:
        result = f.readlines()
        return len(result)

len_list.append(read_and_count('1.txt'))
len_list.append(read_and_count('2.txt'))
len_list.append(read_and_count('3.txt'))
first = min(len_list)
last = max(len_list)

def write_one_txt():
    f = open('result.txt', 'a')
    f.write('1.txt\n')
    f.write(f"{read_and_count('1.txt')}\n")
    f.close()
    f1 = open('1.txt', 'r')
    result = f1.read()
    f = open('result.txt', 'a')
    f.write(f'{result}\n')
    f.close()

def write_two_txt():
    f = open('result.txt', 'a')
    f.write('2.txt\n')
    f.write(f"{read_and_count('2.txt')}\n")
    f.close()
    f1 = open('2.txt', 'r')
    result = f1.read()
    f = open('result.txt', 'a')
    f.write(f'{result}\n')
    f.close()

def write_three_txt():
    f = open('result.txt', 'a')
    f.write('3.txt\n')
    f.write(f"{read_and_count('3.txt')}\n")
    f.close()
    f1 = open('3.txt', 'r')
    result = f1.read()
    f = open('result.txt', 'a')
    f.write(f'{result}\n')
    f.close()

if read_and_count('1.txt') == first:
    write_one_txt()
if read_and_count('2.txt') == first:
    write_two_txt()
elif read_and_count('3.txt') == first:
    write_three_txt()

if read_and_count('1.txt') != first and read_and_count('1.txt') != last:
    write_one_txt()
if read_and_count('2.txt') != first and read_and_count('2.txt') != last:
    write_two_txt()
elif read_and_count('3.txt') != first and read_and_count('3.txt') != last:
    write_three_txt()

if read_and_count('1.txt') == last:
    write_one_txt()
if read_and_count('2.txt') == last:
    write_two_txt()
elif read_and_count('3.txt') == last:
    write_three_txt()


