"""Задача_2. 5 баллов

Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.

Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg

Результат: ['bear', 'milk']"""

spis_1 = input('Введите список через пробел: ').split(' ') # получение списка от пользователя
key_word = input('Введите название элемента, который нужно удалить: ') # получение ключевого слова от пользователя
count = 0 # задаем переменную счетчика совпадений
while key_word in spis_1: # задаем цикл-условие, проверяющий совпадения элементов списка с ключевым словом
    count += 1
    spis_1.remove(key_word) # поочредно удаляем элементы списка, совпавшие с ключевым словом
if count == 0: # проверка на отсутствие совпадений
    print('\nСовпадений не найдено')
else:
    print('\nОбработанный список: ', spis_1) # отображаем обработанный список