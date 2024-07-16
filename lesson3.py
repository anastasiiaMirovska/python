# class User:
#     def __init__(self, user_name):
#         self.__name = user_name
#
#     def __get_name(self):
#         return self.__name
#
#
#     def __set_name(self, user_name):
#         self.__name = user_name
#
#     def __del_name(self):
#         del self.__name
#
#     name = property(fget=__get_name, fset=__set_name, fdel=__del_name)
#
# les = User("Les")
# les.name = "Helo"
# print(les.name)
# del les.name


# class User:
#     def __init__(self, user_name):
#         self.__name = user_name
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, user_name):
#         self.__name = user_name
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# les = User("Les")
# les.name = "Helo"
# print(les.name)
# del les.name


#Singleton

class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

user1 = User("John")
user2 = User("Les")
print(user1.name, user2.name)
