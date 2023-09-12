
# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

def vinni_puh(stih):
    lines = stih.split()
    print(lines)
    syllable_counts = []

    for line in lines:
        syllables = line.split('-')

        syllable_count = sum(1 for s in syllables if any(
            c in 'АЕИОУЫЭЮЯаеиоуыэюя' for c in s))
        syllable_counts.append(syllable_count)

    return all(count == syllable_counts[0] for count in syllable_counts)


stih = input("Введите стихотворение Винни-Пуха: ")
if vinni_puh(stih):
    print("Парам пам-пам")
else:
    print("Пам парам")

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            result = operation(i, j)
            row.append(result)
        print(" ".join(map(str, row)))