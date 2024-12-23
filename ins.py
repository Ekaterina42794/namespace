from encodings.punycode import insertion_sort

from module_42.alg import *
data_1=list(map(int,input('Введите числа через пробел: ').split())) # 1 2 3 4
data_2=list(map(int,input('Введите числа через пробел: ').split()))
data_3=list(map(int,input('Введите числа через пробел: ').split()))
bubble_sort(data_1)
print('пузырьковая сортровка:_ ',data_1)

selection_sort(data_2)
print('сортировка выборок:_ ',data_2)

insertion_sort(data_3)
print('сортровка вставкой:_ ',data_3)

# if __name__ == '__main__':
#     print_hi('PyCharm')

