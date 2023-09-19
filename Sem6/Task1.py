'''
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы
массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
'''
# import random

# list_1 = int(input('Введите кол-во элементов в первом списке: '))
# list_2 = int(input('Введите кол-во элементов во втором списке: '))
# list_empty =[]
# print(n1 := [random.randint(1, 20) for i in range(list_1)])
# print(n2 := [random.randint(1, 10) for i in range(list_2)])

# for i in range(len(n1)):
#     if n1[i] not in n2:
#         list_empty.append(n1[i])
# print(list_empty)
import random

size_1 = int(input('Размер первого списка: '))
size_2 = int(input('Размер второго списка: '))

print(lst_1 := [random.randint(0,10) for _ in range(size_1)])
print(lst_2 := [random.randint(0,10) for _ in range(size_2)])

print([i for i in lst_1 if i not in lst_2])

# for i in lst_1:
# if i not in lst_2:
# lst_3.append(i)