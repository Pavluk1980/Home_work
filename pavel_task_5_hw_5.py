# add
set_1 = set('123')
print(set_1)
set_1.add('4') # Добавляет в множество указанный элемент
print(set_1,'\n')

# clear
set_1 = set('123')
print(set_1)
set_1.clear() # Очищает множество (удаляет все его элементы).
print(set_1,'\n')

# copy
set_1 = set('123')
set_2 = set_1
set_3 = set_1.copy() # Возвращает поверхностную копию множества.
set_1.add('4')
print(set_1) # объект изменился
print(set_2) # объект содержит ссылку на set_1, а значит изменения повлияют на него
print(set_3,'\n') # Объект не изменился

# difference
set_1 = set('12345')
print(set_1)
set_2 = set ('45678')
print(set_2)
print(set_1.difference(set_2),'\n')# Возвращает элементы множества set_1 которые отсутствуют в указанном множестве set_2

# difference_update
set_1 = set('12345')
print(set_1)
set_2 = set ('45678')
print(set_2)
set_1.difference_update(set_2) # Удаляет из множества set_1 все элементы, присутствующие в указанном множестве set_2
print(set_1,'\n')

# discard
set_1 = set('12345')
print(set_1)
set_1.discard('5') # Удаляет указанный элемент, если он присутствует в множестве.
print(set_1,'\n')

# intersection
set_1 = set('12345')
print(set_1)
set_2 = set ('45678')
print(set_2)
print(set_1.intersection(set_2),'\n') # Возвращает множество с элементам присутствующими в обоих множествах.

# intersection_update
set_1 = set('12345')
print(set_1)
set_2 = set ('45678')
print(set_2)
set_1.intersection_update(set_2) # Оставляет в множестве set_1 только те элементы которые входят в его пересечение с указанным множеством set_2
print(set_1,'\n')

# isdisjoint
set_1 = set('12345')
print(set_1)
set_2 = set ('45678')
print(set_2)
set_3 = set ('67890')
print(set_3)
print(set_1.isdisjoint(set_2)) # Возвращает False если у множества set_1 есть общие элементы с указанным множеством set_2
print(set_1.isdisjoint(set_3),'\n') # Возвращает True если у множества set_1 нет общих элементов с указанным множеством set_3

# issubset
set_1 = set('123')
print(set_1)
set_2 = set ('123')
print(set_2)
set_3 = set ('12345')
print(set_3)
set_4 = set ('23456')
print(set_4)
print(set_1.issubset(set_2)) # Возвращает True если множество set_1 эквивалентно указанному множеству set_2 или является его подмножеством.
print(set_1.issubset(set_3)) # Возвращает True если множество set_1 эквивалентно указанному множеству set_2 или является его подмноже
print(set_1.issubset(set_4),'\n')

# issuperset
set_1 = set('12345')
print(set_1)
set_2 = set ('12345')
print(set_2)
set_3 = set ('123')
print(set_3)
set_4 = set ('23456')
print(set_4)
print(set_1.issuperset(set_2)) # Возвращает True если множество set_1 эквивалентно указанному множеству set_2 или является его надмножеством.
print(set_1.issuperset(set_3)) # Возвращает True если множество set_1 эквивалентно указанному множеству set_2 или является его надмноже
print(set_1.issuperset(set_4),'\n')

# pop
set_1 = set('123')
print(set_1)
set_1.pop()
print(set_1)
set_1.pop()
print(set_1)
set_1.pop()
print(set_1)
#set_1.pop()
#print(set_1) # Удаляет и возвращает произвольный элемент множества. Если множество является пустым, то вызывается исключение KeyError.

# remove
set_1 = set('12345')
print(set_1)
set_1.remove('5') # Удаляет указанный элемент x из множества или вызывает исключение KeyError если такой элемент отсутсвует.
print(set_1,'\n')

# symmetric_difference
set_1 = set('12345')
print(set_1)
set_2 = set('45678')
print(set_2)
print(set_1.symmetric_difference(set_2),'\n') # Возвращает элементы которые присутствуют в обоих множествах, кроме тех, которые являются общими.

# symmetric_difference_update
set_1 = set('12345')
print(set_1)
set_2 = set('45678')
print(set_2)
set_1.symmetric_difference_update(set_2) # Добавляет элементы из указанного множества set_1 и удаляет элементы которые являются общими.
print(set_1,'\n')

# union
set_1 = set('12345')
print(set_1)
set_2 = set('45678')
print(set_2)
print(set_1.union(set_2),'\n') # Возвращает объединение множеств.

# update
set_1 = set('12345')
print(set_1)
set_2 = set('45678')
print(set_2)
set_1.update(set_2) # Добавляет в множество set_1 элементы указанного множества set_2
print(set_1)