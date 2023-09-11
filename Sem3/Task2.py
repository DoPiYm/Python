'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
'''

#firstlist = [1,2,3,4,5]
#k = int(input('Введите число сдвига: '))
#print(firstlist)

#for i in range(k):
#    a = firstlist.pop(-1)
#    firstlist.insert(0,a)
#    print(firstlist)

    
#secondlist = firstlist [k:] + firstlist[:k] 
#print (secondlist)


'''
import random 

lst = [random.randint(0,100) for i in range(10)]
print(lst)
shift = int(input('Введите сдвиг: '))

print(lst[:-shift])
print(lst[-shift:])
lst = lst[-shift:] + lst[:-shift]
print(lst)
'''

#Циклический запуск списка

for i in range(500):
    print(lst[i%len(lst)], end=' ')
    фигня