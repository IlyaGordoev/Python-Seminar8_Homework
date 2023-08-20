# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# Выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход


def main_menu(): 
    main_menu = ['1 - Вывести контакты на экран',
             '2 - Добавить контакт',
             '3 - Удалить контакт',
             '4 - Изменить контакт',
             '5 - Найти контакт',
             '6 - Выход']
    print(*main_menu, sep = '\n')

def select(lst):
    select = int(input('\nЧто нужно изменить или ввести:\n\n'
                                   '1-фамилию\n'
                                   '2-имя\n'
                                   '3-отчество\n'
                                   '4-номер телефона\n'
                                   '5-коментарий\n'
                                   '6-следующее совпадение или выход\n\n'))
    if select == 1:
        lst[0] = input('Введите фамилию: ')
    elif select == 2:
        lst[1] = input('Введите имя: ')
    elif select == 3:
        lst[2] = input('Введите отчество: ')
    elif select == 4:
        lst[3] = input('Введите номер телефона: ')
    elif select == 5:
        lst[4] = input('Введите коментарий: ')
    return select

def input_item_selection():
    choice = input('\nВыберите действие: ')
    while not choice.isdigit()or (6 < int(choice) or int(choice) < 1):
        choice = input('\nВведите от 1-6: ')
    else:
        return int(choice)

def read():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        data = file.read()
        print(f'\n{data} \n')

def append():
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(input('Введите фамилию: ') + ' ')
        file.write(input('Введите имя: ') + ' ')
        file.write(input('Введите отчество: ')+ ' ')
        file.write(input('Введите номер телефона: ') + ' ')
        file.write(input('Введите комментарий: ') + '\n')

def delete(item):
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lst = data.readlines()
        for i in range(len(lst)):
            if item in lst[i%len(lst)].lower().split():
                lst.pop(i)
    with open('phonebook.txt', 'w', encoding='utf-8') as data:
        data.writelines(lst)

def change(item):
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        lst = data.readlines()
        for i in range(len(lst)):
            if item in lst[i%len(lst)].lower().split():
                print('\nЭтот контакт нужно изменить?')
                lst2 = list(lst[i].split())
                print(*lst2, sep= ' ')
                select(lst2)
                print(*lst2, sep = ' ')
                lst2 = ' '.join(lst2) + '\n'
                lst[i] = lst2
                with open('phonebook.txt', 'w', encoding='utf-8') as data:
                    data.writelines(lst)
    

def find(item):
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if item in line.lower().split():
                print(f'\n{line}')
  
def choice_menu(a):
    if a == 1:
        read()
    elif a == 2:
        append()
    elif a == 3:
        searh_item = input('\nВведите кого нужно удалить: ').lower()
        delete(searh_item)
    elif a == 4:
        searh_item = input('\nВведите кого нужно заменить: ').lower()
        change(searh_item)
    elif a == 5:
        searh_item = input('\nВведите что ищете: ').lower()
        find(searh_item)
    elif a == 6:
        exit()


while True:
    main_menu()
    item = input_item_selection()
    choice_menu(item)