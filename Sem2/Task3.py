'''
Иван Васильевич пришел на рынок и решил купить два арбуза:
один для себя, а другой для тещи. Понятно,
что для себя нужно выбрать арбуз потяжелей,
а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий
и самый тяжелый арбуз? Помогите ему!
'''

import random

watermelon = int(input('Количество арбузов: '))
minimal = 30000
maximal = 1000

for i in range(watermelon):
    weight = random.randint(1000, 30000)
    print(weight)
    if weight < minimal:
        minimal = weight
    if weight > maximal:
        maximal = weight
print(f"Мой = {maximal}, а тёщин = {minimal}")