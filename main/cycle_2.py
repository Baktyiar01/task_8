#2. Найдите сумму всех элементов списка [1, '2', 3, 4, '5'], предварительно приводя строки к целым числам

number_list = [1,'2',3, 4,'5']

number_list_1 = [int(i) for i in number_list]

print(sum(number_list_1))