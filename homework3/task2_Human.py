# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, foot_size) -> None:
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls) -> None:
        print(f"Class Cinderella has {cls.__count} instances")

    def __repr__(self) -> str:
        return f'{self.name} is {self.age} years and {self.foot_size} foot'


class Prince(Human):
    def __init__(self, name: str, age: int, found_foot_size) -> None:
        super().__init__(name, age)
        self.found_foot_size = found_foot_size

    def find_cinderella(self, cinderellas: list[Cinderella]) -> Cinderella | str:
        # wife = [cinderella for cinderella in cinderellas if cinderella.foot_size == self.found_foot_size]
        wife = None
        for cinderella in cinderellas:
            if cinderella.foot_size == self.found_foot_size:
                wife = cinderella
                break
        if wife is not None:
            return wife
        else:
            return "No cinderella"


cinderellas_list: list[Cinderella] = [
    Cinderella('Angela', 23, 39),
    Cinderella('Amy', 25, 38),
    Cinderella('Agata', 21, 37),
    Cinderella('Anastasiia', 24, 35),
    Cinderella('Ann', 28, 35),
    Cinderella('Emily', 29, 40),
]

Cinderella.get_count()

prince = Prince('Wilgelm', 25, 35)
print(prince.find_cinderella(cinderellas_list))
