# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

from random import randint
n = int(input('Введите количество элементов массива: '))
left = int(input('Введите левую границу диапазона значений: '))
right = int(input('Введите правую границу диапазона значений: '))
x = int(input('Введите искомое число: '))
A = [randint(left, right) for i in range(n)]
print(A)
diff, result = abs(x - A[0]), A[0]
for i in A:
    if abs(x - i) < diff:
        diff, result = abs(x - i), i
    elif abs(x - i) == diff:
        diff_2, result_2 = abs(x - i), i
if diff == diff_2 and result != result_2:
    print(f'Ближайшие к искомому числу: {result} и {result_2}.')
else:
    print(f'Ближайшее к искомому числу: {result}.')