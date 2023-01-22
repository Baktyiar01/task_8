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
