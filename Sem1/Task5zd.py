"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

# n = 123

# Введите ваше решение ниже

#n = int(input('Введите трехзначное число: ') #мое решение

#c = n % 10 
#n = n // 10
#b = n % 10
#a = n // 10

#print ( a + b + c)

#n1 = n // 100 # Нахождение первой цифры числа
#n2 = (n % 100) // 10 # Нахождение второй цифры числа
#n3 = n % 10 # Нахождение третьей цифры числа
#res = n1 + n2 + n3

"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

# n = 6

# Введите ваше решение ниже
#n = 90
#print ("Петя и Сережа сделали", n/6, "шт") #мое решение
#print ("Маша сделала", n/6*4, "шт")

#1 = n // 6
#n2 = n // 6
#n3 = (n // 6) * 4
#print(n1, n3, n2)

"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

# n = 385916

# Введите ваше решение ниже
'''
n = input('Введите число: ')
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
  print("YES")
else:
  print("NO")
'''
t = input('Введите номер билета: ')
l = int(t[0]) + int(t[1]) + int(t[2])
r = int(t[3]) + int(t[4]) + int(t[5])
if l == r:
    print('Yes')
else:
    print('NO')
# или
s = input('Введите 6-значный номер билета: ')
if len(s) != 6:
    print(f'Число {s} не 6-ти значное')
else:
    res1 = 0
    res2 = 0
    for i in range(len(s)//2):
        res1 += int(s[i])
        res2 += int(s[len(s)//2 + i])
    if res1 == res2:
        print(f'{s} счастливый номер')
    else:
        print(f'{s} не счастливый номер')