def dashed_line():
    print("-----------------------------------------------------\n")


def print_menu():
    dashed_line()
    print("Робота із масивом: \n",
          my_list,
          "\n\t1 - Знайти мінімальне число\n"
          "\t2 - Видалити усі дублікати \n"
          "\t3 - Замінити кожне четверте значення на Х")
    print("4 - Вивести на екран квадрат із зірочок за заданою стороною")
    print("5 - Вивести табличку множення")
    print("6 - Завершити роботу")
    dashed_line()


def find_min(array):
    print(f"Масив {array} має найменше значення: ", min(array))


def delete_duplicates(array):
    unique_array = []
    for item in array:
        if item not in unique_array:
            unique_array.append(item)
    print("Масив до змін: \n", array)
    print("Масив без повторюваних значень: \n", unique_array)
    return unique_array


def change_each_four(array):
    changed_array = []
    for index, value in enumerate(array):
        if index != 0 and (index + 1) % 4 == 0:
            changed_array.append("X")
        else:
            changed_array.append(value)
    print("Масив до змін: \n", array)
    print("Новий масив: \n", changed_array)
    return changed_array


def print_square():
    side = input("Введіть розмір сторони квадрата: ")
    star = "*"
    space = " "
    if not side.isnumeric() or side == "0":
        print("Неправильно вказані дані. Спробуйте ще раз:\n")
        print_square()
    else:
        side = int(side)
        if side == 1:
            print(star)
        else:
            print((star + space * 2) * side)
            for i in range(side - 2):
                print(star + space * 3 * (side - 2) + space * 2 + star)
            print((star + space * 2) * side)


def multiplication_table():
    number = 1
    while number < 9:
        i = 1
        number_array = []
        while i <= 9:
            number_array.append(f"{number * i:3}")  # Форматуємо числа з вирівнюванням по 3 символи
            i += 1
        print(" ".join(number_array))
        number += 1


my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

play = True
while play:
    print_menu()
    choice = input("Виберіть номер: ")
    match choice:
        case "1":
            find_min(my_list)
        case "2":
            new_array = delete_duplicates(my_list)
            my_list = new_array[::]
        case "3":
            new_array = change_each_four(my_list)
            my_list = new_array[::]
        case "4":
            print_square()
        case "5":
            multiplication_table()
        case "6":
            print("Кінець. Дякую за співпрацю!")
            play = False
        case _:
            print("Неправильне число. Спробуйте ще раз")
            continue
