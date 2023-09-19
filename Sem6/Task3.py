'''
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
'''

import random

print(lst := [random.randint(0,10) for _ in range (15)])

count = 0 

for item in set(lst):
    count += lst.count(item) // 2

print(count)