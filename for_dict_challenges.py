# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
# ???

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

#Option 1:
names = {}
for number in range(len(students)):
    if students[number]['first_name'] in names:
        names[students[number]['first_name']] += 1
    else:
        names[students[number]['first_name']] = 1 
print(names)

#Option 2:
import collections
c = collections.Counter()
for number in range(len(students)):
    f_name = students[number]['first_name']
    c[f_name] += 1
print(c)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

#Option 1
names = {}
for number in range(len(students)):
    if students[number]['first_name'] in names:
        names[students[number]['first_name']] += 1
    else:
        names[students[number]['first_name']] = 1 
names_1 = sorted(names.items(), key=lambda item: item[1], reverse=True)
print(f'Самое частое имя среди учеников: {names_1[0][0]}')

#Option 2
c = collections.Counter()
for number in range(len(students)):
    f_name = students[number]['first_name']
    c[f_name] += 1
c_sorted = sorted(c.items(), key=lambda item: item[1], reverse=True)
print(f'Самое частое имя среди учеников: {c_sorted[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

#Option 1
for class_number in range(len(school_students)):
    names = {}
    for number in range(len(school_students[class_number])):
        if school_students[class_number][number]['first_name'] in names:
            names[school_students[class_number][number]['first_name']] += 1
        else:
            names[school_students[class_number][number]['first_name']] = 1
    names_sorted = sorted(names.items(), key=lambda item: item[1], reverse=True)
    print(f'Самое частое имя в классе {class_number+1}: {names_sorted[0][0]}')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for class_number in range(len(school)):
    males = 0
    females = 0
    for student in range(len(school[class_number]['students'])):
      class_n = school[class_number]['class']
      name = school[class_number]['students'][student]['first_name']
      if is_male[name] == True:
        males += 1
      else:
        females += 1
       
    print(f'В классе {class_n} {females} девочек и {males} мальчиков')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

classes = []
for class_number in range(len(school)):
    class_i = {}
    males = 0
    females = 0
    class_n = school[class_number]['class']
    for student in range(len(school[class_number]['students'])):
      name = school[class_number]['students'][student]['first_name']
      if is_male[name] == True:
        males += 1
      else:
        females += 1
    class_i['class_number'] = class_n
    class_i['males'] = males
    class_i['females'] = females
    classes.append(class_i)

most_males = sorted(classes, key=lambda x: x['males'], reverse=True)[0]['class_number']
most_females = sorted(classes, key=lambda x: x['females'], reverse=True)[0]['class_number']
   
print(f'Больше всего мальчиков в классе {most_males}')
print(f'Больше всего девочек в классе {most_females}')