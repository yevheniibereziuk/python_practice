#masivu 

from calendar import c
from operator import le


cities = ['New York', 'Ukraine', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities))
print(cities[0])
print(cities[-1]) # c k конца массива будет напечатан первый 
print(cities[-2])
print(cities[2].upper())

cities[2] = 'Dnepr'
print(cities)

cities.append('Lviv')
cities.append('Yalta')
print(cities)

cities.insert(2, 'Feodosiya')
print(cities)


del cities[-1] #  удаляет значение из массива
print(cities)

cities.remove('Ukraine') # найдет  указанное значение и стерет его 
print(cities)

deleted_city = cities.pop()
print("Deleted city is: " + deleted_city)
print(cities)

cities.sort(reverse=True) #  сортирует массив в обратном порядке 
print(cities)

cities.reverse()
print(cities)