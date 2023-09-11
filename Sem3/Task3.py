'''
Дан cписок, состоящий из целых чисел. Напишите программу,
которая подсчитает количество элементов массива, больших
предыдущего (элемента с предыдущим номером)
'''
import random 

lst = [random.randint(0,10) for i in range(10)]
count = 0
for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        count += 1
print(count)
