# var = "Max"
# def a():
#     var = "Bob"
#     def b():
#         var="Petro"
#         def c():
#             nonlocal var
#             var = "Mary"
#             print(var)
#         c()
#         print(var)
#     b()
#     print(var)
#
#
# a()
# print(var)
# print(globals())


# def test():
#     name = 'Max'
#
#     def get_name():
#         return name
#
#     def set_name(new_name):
#         nonlocal name
#         name = new_name
#
#     return [get_name, set_name]
#
# get_name, set_name = test()
#
# print(get_name())
# set_name("Kira")
# print(get_name())

# users = [
#     {"name": "John", "age": 12},
#     {"name": "John", "age": 2},
#     {"name": "John", "age": 92},
#     {"name": "John", "age": 26}
# ]
# print(sorted(users, key = lambda item: item["age"]))

# a = 9
# b = 10
# a, b = b,a
# print(a, b)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = [*l]
# a, b, *_, c = l
# print(a, b, c)


# d = {
#     "name": "Max",
#     "age":18
# }
#
# d2 = {**d}

# def star_decorator(func):
#     def inner(*args, **kwargs):
#         print("*"*20)
#         func(*args, **kwargs)
#         print("*" * 20)
#     return inner
#
# @star_decorator
# def greeting(name):
#     print(f"Hello, {name}")
#
# greeting("Bob")
#
# my_inner = star_decorator(greeting)
# my_inner(("Les"))


# name = "Anastasiia"
# def my_func():
#     global name
#     print(name)
#
# my_func()


# def counter():
#     count = 0
#
#     def inc():
#         nonlocal count
#         count += 1
#         return count
#
#     def reset():
#         nonlocal count
#         count = 0
#
#     return inc, reset
#
# inc1, reset1 = counter()
# inc2, reset2 = counter()
#
# print(inc1())
# print(inc2())
# print(inc1())
# print(inc1())
# print(inc2())
#
# reset1()
# reset2()
#
# print(inc1())
# print(inc2())



# a: str = 123
# print(a)

# def my_func(string_list: list[str]):
#     string_list.sort()



# def my_func(int_list: list[int|float]) -> int | float:
#     return sum(int_list)


# t: tuple[int, str, float]= (1, "st", 3.2)

# t: tuple[int,...] = (1,2,3,4,5,6,7,8,9)


import typing
User = typing.TypedDict("User", {"name": str, "age": int, "status":bool})

user: User = {
    "name": "Les",
    "age": 20,
    "status":True
}