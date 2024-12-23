print("Пузырьковая сортировка")
nums = [5, 7, 9, 2, 1, 4, 3, 6, 8]


def bubble_sort(ls):    # пузырьковая сортировка o(n2)
    swapped = True      # поменялись местами = True
    while swapped:      # пока поменялись местами
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1]= ls[i+1], ls[i]
                swapped = True
print(nums)
bubble_sort(nums)
print(nums)
print('__________')

print(" сортировка Выборка")
nums_1 = [4, 3,5, 7, 9, 1,2,  6, 8]
def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i          # самый низкий=i
        for j in range(i+1, len(ls)):
            if ls[j]<ls[lowest]:
                lowest=j
        ls[i],ls[lowest]=ls[lowest] ,ls[i]
print(nums_1)
selection_sort(nums_1)
print(nums_1)