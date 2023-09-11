'''
Дан список чисел. Определите, сколько в нем встречается различных чисел.
'''

mylist = [1,5,4,2,5,6,7,9,10]
print(mylist)
mylist = set(mylist)
print(len(mylist))