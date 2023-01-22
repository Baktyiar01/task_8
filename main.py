
# Линейные алгоритмы

# 1.Перевести граммы в килограммы и вывести результат на экран. Значение граммов ввести с клавиатуры.

# gramm = int(input('Enter the sum of gramms: '))

# result = gramm / 1000
# print(result)

# 2.Даны две переменные x = 10 и y = 55. Поменяйте их значения местами. 
# Выведите значения переменных на экран до и после замены.

# x = 10
# y = 55

# print(f' {x, y}, {y, x}')


# 3. С клавиатуры вводится расстояние L в метрах. Необходимо найти и вывести на экран количество полных километров в нем.

# l = int(input('Enter a distance in meters: '))

# km = l // 1000
# print(km)

# # 4. С клавиатуры вводится целое число. Необходимо вывести число, обратное введенному по порядку составляющих его цифр. 
# Например, если было введено число 12345, программа должна вывести пользователю на экран число 54321.

# number = input('Enter the number: ')

# reverse_number = []
# new_number = ''

# for n in number:
#     reverse_number.insert(0, n)

# for n in reverse_number:
#     new_number += n

# print(f'Перевернутый {new_number} ')


# 5.Получите и преобразуйте текущую системную дату, возвращаемую методом date.today() модуля стандартной библиотеки datetime,
# из формата «год-месяц-день» в формат «день.месяц.год». Выведите оба формата даты на экран.

# import datetime

# date_1 = datetime.date.today()
# date_2 = datetime.date.today(). strftime("%d.%m.%Y")

# print(f' {date_1}, {date_2} ')


# Логические выражения

# 1. Записать и вывести на экран условие, которое является истинным, когда хотя бы одно из чисел x, y и z больше 80.

# x = 10
# y = 50
# z = 75

# if x > 80 or y > 80 or z > 80:
#     print(True)
# else:
#     print()

    
# 2. Записать и вывести на экран условие, которое является истинным, когда оба числа a и b одновременно положительны или отрицательны.

# a = 5
# b = 10

# if a >= 0 and b >=0:
#     print(True)
# elif a < 0 and b < 0:
#     print(True)
# else:
#     print()


# 3. Даны три числа: 130, 25 и 70. Выведите на экран наименьшее из них, использовав для этого программную проверку.

# a = 130
# b = 25
# c = 70

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# elif c < a and c < b:
#     print(c)
# else:
#     print()

# Циклы

#  1. Посчитайте количество символов в строке 'Python - это Питон!', использовав счетчики на основе циклов for и while.

# text = 'Python - это Питон!'

# while text.isalpha():
#     print(len(text))


#2. Найдите сумму всех элементов списка [1, '2', 3, 4, '5'], предварительно приводя строки к целым числам

# number_list = [1,'2',3, 4,'5']

# number_list_1 = [int(i) for i in number_list]

# print(sum(number_list_1))

# 3.Используя циклы, проверьте при помощи оператора in наличие символов строки 'abcde123' в строке 'bad_cat_23', 
# выводя результаты проверки на экран в виде «Символ "a" есть в "bad_cat_23".» или «Символа "n" нет в "bad_cat_23".».

list_1 = 'abcde123'
list_2 = 'bad_cat_23'

if list_1[0] in list_2:
    print(f'Символ "{list_1[0]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[0]}" нет в "{list_2}"')

if list_1[1] in list_2:
    print(f'Символ "{list_1[1]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[1]}" нет в "{list_2}"')

if list_1[2] in list_2:
    print(f'Символ "{list_1[2]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[2]}" нет в "{list_2}"')

if list_1[3] in list_2:
    print(f'Символ "{list_1[3]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[4]}" нет в "{list_2}"')

if list_1[4] in list_2:
    print(f'Символ "{list_1[4]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[4]}" нет в "{list_2}"')

if list_1[5] in list_2:
    print(f'Символ "{list_1[5]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[5]}" нет в "{list_2}"')

if list_1[6] in list_2:
    print(f'Символ "{list_1[6]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[6]}" нет в "{list_2}"')

if list_1[-1] in list_2:
    print(f'Символ "{list_1[-1]}" есть в "{list_2}"')
else:
    print(f'Символ "{list_1[-1]}" нет в "{list_2}"')


# 4. Cгенерируйте и выведите на экран мозаичное изображение гексагональной сетки, напоминающее мелкоячеистую проволочную сетку.
x_size = 15
y_size = 10

for i in range(y_size):
    for x in range(x_size):
        print(r'/ \_', end='')
    print()
    for x in range(x_size):
        print(r'\_/ ', end='')
    print()
