# from pathlib import Path


def read_tel(telephone_book):
    with open(telephone_book, 'r', encoding='utf-8') as txt_file:
        for line in txt_file:
            print(line.strip())


def add_tel(telephone_book):
    family_name = input('Family: ')
    name = input('Name: ')
    surname = input('surname: ')
    res = f' \n {family_name},{name},{surname}'
    with open(telephone_book, 'a', encoding='utf-8') as txt_file:
        txt_file.write(res)


def find_abonent(telephone_book):
    item = input('Что ищем: ')
    item_type = int(
        input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    with open(telephone_book, 'a', encoding='utf-8') as txt_file:
        count = 0
        for line in txt_file:
            result = line.split()
            if item.lower() in result[item_type].lower():
                print(*line)
                count += 1
        if count == 0:
            print('Нет такого абонента')


# find_abonent('tel.txt')
# read_tel('tel.txt')
# add_tel('tel.txt')


def edit_abonent(telephone_book):
    item = input('Что редактируем: ')
    item_type = int(
        input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))
    new_data = input('Введите новые данные: ')

    with open(telephone_book, 'r+', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
        found = False

        for i, line in enumerate(lines):
            result = line.split()

            if item.lower() in result[item_type].lower():
                print('Редактирование абонента:', *result)

                result[item_type] = new_data
                lines[i] = ' '.join(result) + '\n'
                print('Отредактированные данные:', ' '.join(result))
                found = True

        if not found:
            print('Нет такого абонента')
        txt_file.seek(0)
        txt_file.writelines(lines)
        txt_file.truncate()


# edit_abonent('tel.txt')


def delete_abonent(telephone_book):
    item = input('Что удаляем: ')
    item_type = int(
        input('Введите номер (0-фамилия, 1-имя, 2-отчество, 3-телефон): '))

    with open(telephone_book, 'r+', encoding='utf-8') as txt_file:
        lines = txt_file.readlines()
        found = False
        for i, line in enumerate(lines):
            result = line.split()

            if item.lower() in result[item_type].lower():
                print('Удален абонент:', *result)
                lines.pop(i)
                found = True

        if not found:
            print('Нет такого абонента')

        txt_file.seek(0)
        txt_file.writelines(lines)
        txt_file.truncate()


delete_abonent('tel.txt')
