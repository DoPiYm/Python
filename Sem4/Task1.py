'''
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
'''

some_string = input ('Ввелите строку: ')

dict_count = {}
result_list = []

for i in some_string:
    if i in dict_count:
        dict_count[i] = dict_count.get(i) + 1
    else: 
        dict_count[i] = 1
    if dict_count.get(i) > 1:
        result_list.append(f'{i}_{dict_count.get(i) - 1}')
    else:
        result_list.append(i)

print(*result_list)