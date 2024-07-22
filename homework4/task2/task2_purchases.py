# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
# функціонал:
#  * вивід всіх покупок
#  * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь-якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)

from typing import TypedDict

Note = TypedDict('Note', {"id": str, "name": str, "price": str})


def dashed_decor(func):
    def wrapper(*args, **kwargs):
        print("_"*30)
        func(*args, **kwargs)
        print("_" * 30)
    return wrapper


class NoteBook:
    def __init__(self, file_name):
        self.__notes_list: [Note] = []
        self.__file_name = file_name
        self.__read_file()
        self.__menu()

    def __read_file(self):
        try:
            with open(self.__file_name, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    my_data = line.strip().split()
                    self.__notes_list.append({"id": my_data[0], "name": my_data[1], "price": my_data[2]})

        except FileNotFoundError:
            self.__write_file()
        except Exception as error:
            print(error)

    def __write_file(self):
        with open(self.__file_name, 'w') as f:
            for note in self.__notes_list:
                print(f"{note['id']} {note['name']} {note['price']} ", end="\n", file=f)

    def __list_is_empty(self):
        if len(self.__notes_list) == 0:
            print("There are no purchases")
            return True

    @staticmethod
    def __int_input(prompt: str):
        while True:
            answer = input(prompt)
            if answer.isdigit():
                return answer
            else:
                print("Wrong input type.Try again.")

    @dashed_decor
    def __add_note(self):
        while True:
            pk = self.__int_input("Enter id of the purchase: ")
            if pk in self.__notes_list:
                print("This id already exists. It must be unique.")
            else:
                break
        name = input("Enter name of the purchase: ")
        price = self.__int_input("Enter price of the purchase: ")
        self.__notes_list.append({"id": pk, "name": name, "price": price})
        self.__write_file()

    @dashed_decor
    def __show_all(self):
        if not self.__list_is_empty():
            for note in self.__notes_list:
                print(f"Purchase {note['id']} - {note['name']} - {note['price']} UAH")

    @dashed_decor
    def __delete_note(self):
        pk = self.__int_input("Enter id of the purchase to delete: ")
        exists: bool = False
        for number, note in enumerate(self.__notes_list):
            if note['id'] == pk:
                exists = True
                del self.__notes_list[number]
                self.__write_file()
                print(f"Purchase {note['id']} was successfully deleted.")
        if not exists:
            print(f"Purchase with id = {pk} does not exist.")

    @dashed_decor
    def __find_most_expensive(self):
        if not self.__list_is_empty():
            max_expensive = 0
            item_number = 0
            for number, note in enumerate(self.__notes_list):
                if int(note['price']) > max_expensive:
                    max_expensive = int(note['price'])
                    item_number = number
            print(
                f"The most expensive purchase was :\n{self.__notes_list[item_number]['id']} - "
                f"{self.__notes_list[item_number]['name']} - {self.__notes_list[item_number]['price']} UAH.")

    @dashed_decor
    def __search(self):
        if not self.__list_is_empty():
            query = input("Enter the query: ")
            for number, note in enumerate(self.__notes_list):
                if query == note['id'] or query == note['name'] or query == note['price']:
                    print(f"Purchase: id-{note['id']} - {note['name']} - {note['price']} UAH")

    @dashed_decor
    def __menu(self):
        while True:
            print("1. Show all purchases\n"
                  "2. Add a new purchase\n"
                  "3. Search for a purchase\n"
                  "4. Find the most expensive\n"
                  "5. Delete by id\n"
                  "6. Exit the program\n")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    self.__show_all()
                case 2:
                    self.__add_note()
                case 3:
                    self.__search()
                case 4:
                    self.__find_most_expensive()
                case 5:
                    self.__delete_note()
                case 6:
                    break
                case _:
                    print("Invalid inpt. Try again")


note1 = NoteBook("data2.txt")
note2 = NoteBook("data3.txt")
