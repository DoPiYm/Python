import random

MAX = 10
MIN = -10
days = int(input('Количество наблюдаемых дней: '))
count = 0
max_count = 0
for i in range(days):
    temp = random.randint(MIN, MAX)
    print(temp, end=' ')
    if temp > 0:
        count += 1
        if max_count < count:
            max_count = count
    else:
        count = 0
print(f'\nМаксимально количество теплых дней за период было {max_count}')