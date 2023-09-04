
# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a1 = float(input("Введите первый элемент прогрессии (a1): "))
d = float(input("Введите разность прогрессии (d): "))
n = int(input("Введите количество элементов в прогрессии (n): "))

progression = []

for i in range(n):
    an = a1 + i * d
    progression.append(an)

print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
def find_indices_in_range(arr, min_value, max_value):
    indices = []

    for i, element in enumerate(arr):
        if min_value <= element <= max_value:
            indices.append(i)

    return indices


my_list = [1, 5, 3, 8, 2, 7, 4]
min_value = 2
max_value = 6

result = find_indices_in_range(my_list, min_value, max_value)
print("Индексы элементов в заданном диапазоне:", result)
