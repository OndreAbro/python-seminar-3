# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.

n = int(input('Введите количество элементов массива: '))
A = []
for i in range(n):
    A.append(int(input(f'Введите {i + 1}-й элемент массива: ')))
x = int(input('Введите искомое число: '))
count = 0
for i in A:
    if i == x:
        count += 1
# print(A)
print(f'Число {x} встречается в массиве {count} раз.')