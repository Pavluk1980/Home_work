"""Задача_4 25 баллов

написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается

методы без подчеркиваний. Фунции dir()

т.е для объекта set должен быть список методов"""

a = '-' # вводим признак правильности ввода названия класса
while a == '-': # задаем цикл-условия для проверки правильности ввода
    obj_str = input('Введите название класса объекта ('
                    'int, float, bool, str, list, tuple, set, frozenset, dict): ')  # принимаем название класса объектов от пользователя в вид
    if obj_str == 'int': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = 0
        a = '+'
    elif obj_str == 'float': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = 0.0
        a = '+'
    elif obj_str == 'bool': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = True
        a = '+'
    elif obj_str == 'str': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = str()
        a = '+'
    elif obj_str == 'list': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = []
        a = '+'
    elif obj_str == 'tuple': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = ()
        a = '+'
    elif obj_str == 'set': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = set()
        a = '+'
    elif obj_str == 'frozenset': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = frozenset()
        a = '+'
    elif obj_str == 'dict': # в зависимости от введенного значения преобразовываем переменную в соответсвующий класс
        obj = {}
        a = '+'
    else: print('\nВы ввели неверное название класса объекта. Пожалуйста, повторите ввод.\n')
list_dir = dir(obj) # формируем список методов для данного класса бъектов
key_str = ('_') # ключевой символ для отделения доступных методов от остальных
for i in range(len(list_dir)): # создаем цикл длиной в общее кол-во методов для класса
    if list_dir[0].startswith(key_str): # проверяем нулевой элемент списка на наличие символа "_"
        del list_dir[0] # удаляем нулевой элемент списка в случае наличия символа "_", возвращаемся в начало цикла
print(f'\nДоступные методы для объектов  {type(obj)} - \n{list_dir}') # вывод результата на экран