'''
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
у которых два соседних и, при этом, оба соседних элемента меньше данного.
'''
import random

print(lst := [random.randint(0,10) for _ in range (15)])

count = 0

for i in range(1, len(lst) - 1):
    if lst[i-i] < lst[i] > lst [i+1]:
        count += 1
print(count)