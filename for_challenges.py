# Задание 1 
# Необходимо вывести имена всех учеников из списка с новой строки 
names = ['Оля', 'Петя', 'Вася', 'Маша'] 
for name in names:
    print(name)
    
# Задание 2 
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём. 
names = ['Оля', 'Петя', 'Вася', 'Маша'] 
for name in names:
    print(f'{name}: {len(name)} буквы')
    
# Задание 3 
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика 
is_male = { 
'Оля': False,  # если True, то пол мужской 
'Петя': True, 
'Вася': True, 
'Маша': False, 
} 
names = ['Оля', 'Петя', 'Вася', 'Маша'] 
for name in names:
    print(f'{name} - {is_male[name]}'.replace('False','жен').replace('True','муж'))
    
# Задание 4 
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней 
# Пример вывода: 
# Всего 2 группы. 
# В группе 2 ученика. 
# В группе 3 ученика. 
groups = [ 
['Вася', 'Маша'], 
['Оля', 'Петя', 'Гриша'], 
] 
print(f'Всего {len(groups)} группы.')
for group in range(len(groups)):
    print(f'В группе {len(groups[group])} ученика.')

# Задание 5 
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят. 
# Пример: 
# Группа 1: Вася, Маша 
# Группа 2: Оля, Петя, Гриша 

groups = [ 
    ['Вася', 'Маша'], 
['Оля', 'Петя', 'Гриша'], 
] 
for group in range(len(groups)):
    print(f'Группа {group+1}: {groups[group]}')
  