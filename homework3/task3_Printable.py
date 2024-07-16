# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуються від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є
# класом Book або Magazine інакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")


class Magazine(Printable):
    def __init__(self, name: str):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")


class Main:

    def __init__(self, printable_list: list[Printable] = None):
        if printable_list is None:
            printable_list = []
        self.printable_list = printable_list

    def add(self, other: Printable):
        if isinstance(other, Printable):
            self.printable_list.append(other)

    def show_all_books(self):
        for book in self.printable_list:
            if isinstance(book, Book):
                book.print()

    def show_all_magazines(self):
        for magazine in self.printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()


my_list = [
    Book("Harry Potter"),
    Magazine("Forbes"),
    Magazine("Time"),
    Magazine("People"),
    Book("Alice in Wonderland"),
    Magazine("Fortune"),
    Book("The Little Prince")
]
main = Main(my_list)

main.add(Book("Harry Potter2"))
main.show_all_books()
main.show_all_magazines()
