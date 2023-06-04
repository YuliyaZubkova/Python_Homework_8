# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

import csv

PHONEBOOK_FILE = 'phonebook.txt'


def load_phonebook():
    phonebook = []
    with open(PHONEBOOK_FILE, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            phonebook.append(row)
    return phonebook


def save_phonebook(phonebook):
    with open(PHONEBOOK_FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(phonebook)


def print_phonebook(phonebook):
    for record in phonebook:
        print('Фамилия:', record[0])
        print('Имя:', record[1])
        print('Отчество:', record[2])
        print('Номер телефона:', record[3])
        print('------------------------------')


def search_phonebook(phonebook, query):
    results = []
    for record in phonebook:
        if query.lower() in record[0].lower() or query.lower() in record[1].lower() or query.lower() in record[
            2].lower():
            results.append(record)
    return results


def add_record(phonebook):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_record = [last_name, first_name, middle_name, phone_number]
    phonebook.append(new_record)
    save_phonebook(phonebook)
    print('Запись добавлена успешно.')


def change_person(phonebook, query):
        for record in phonebook:
            if query.lower() in record[0].lower() or query.lower() in record[1].lower() or query.lower() in record[
                2].lower():
                phonebook.remove(record)
                last_name = input('Введите новые данные. Фамилия:  ')
                first_name = input('Имя: ')
                middle_name = input('Отчество: ')
                phone_number = input('Номер телефона: ')
                new_record = [last_name, first_name, middle_name, phone_number]
                phonebook.append(new_record)
                save_phonebook(phonebook)
                print('Запись успешно изменена')


def delete_person(phonebook, query):
    for record in phonebook:
        if query.lower() in record[0].lower() or query.lower() in record[1].lower() or query.lower() in record[
            2].lower():
            res_1 = input(f'Введите 0, если действительно хотите удалить данную запись? {record}')
            if res_1 == ('0'):
                phonebook.remove(record)
                print('Данная запись удалена')
            else:
                print('Данная запись не удалена')


def menu():
    phonebook = load_phonebook()
    while True:
        print('==== Телефонный справочник ====')
        print('1. Вывести все записи')
        print('2. Поиск записей')
        print('3. Добавить запись')
        print('4. Изменить запись')  # change
        print('5. Удалить запись')
        print('0. Выйти')
        choice = input('Введите номер действия: ')
        print()
        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            query = input('Введите фамилию, имя или отчество для поиска: ')
            results = search_phonebook(phonebook, query)
            if results:
                print('Результаты поиска:')
                print_phonebook(results)
            else:
                print('Нет совпадений.')
        elif choice == '3':
            add_record(phonebook)
        elif choice == '4':
            query = input('Введите фамилию человека, чью запись нужно изменить: ')
            results = search_phonebook(phonebook, query)
            if results:
                change_person(phonebook, query)
            else:
                print('Нет совпадений.')

        elif choice == '5':
            query = input('Введите фамилию человека, запись которого нужно удалить: ')
            if search_phonebook(phonebook, query):
                delete_person(phonebook, query)
            else:
                print('Нет совпадений.')
        elif choice == '0':
            break
        else:
            print('Неверный выбор. Пожалуйста, повторите.')


menu()
