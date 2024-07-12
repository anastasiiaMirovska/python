
# d = {"bob": "hello", "john": "world"}
# d.update({"john": "hello"})
# print(d)

#l = [1, 3 , 4 , 5, 1]
# l.insert(3, 1)
# print(l)
#
# se = {1,2,9,3,8,0}
# print(se)
# se.pop()
# print(se)

# l = [1,2, 3, 4, 5, 6]
# a, *_, b = l
# print(a, b, _)
#
#
# d = {
#     "name": "Bob",
#     "age":18,
#     "status": False
# }
#
# def test(name, age, sta):
#     print(name, age, sta)
#
# def test2(**kwargs):
#     print(kwargs)
#
# test2(**d)



# name = "Max"
# age = 18
# print("name = %s,  age = %d" % (name, age))
#
# print("name = %(n)s,  age = %(a)d" % {"n": name, "a": age})
#
# print("name = {},  age = {}".format(name, age))
# print("name = {n},  age = {a}".format(n=name, a=age))
#
# print(f"name = {name}, age = {age}")



# list1 = [1,2,3,4,5]
# list2 = list(list1)
# list3 = list1[:]
# list4 = list1.copy()

# name = "Bob"
# name.center(5,"*")
# print(name) #           *Bob*


# list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(list1[10:2:-1])
# print(list1[::3])


# t = 1, 3, 7, 2
# t = (1, 3, 7, 2)
# t = ("s",)
# print(type(t))

# d = dict(name='Bob', age=250)
# print(d['age'])

# d = dict ([('name', 'Bob'), ('age', 25)])

# d = dict.fromkeys([1, 'www','name'],123)
# print(d)

# d ={
#     "name": "Bob",
#     "age": 25
# }
# print(d)


# my_set = {1,3,0}
# print(my_set)

# set1 = {1, 2, 18, 23, 31}
# set2 = {1, 2, 3, 4, 5}

# set1.symmetric_difference_update(set2)
# print(set1)


# print(set1.difference(set2))

# set1.difference_update(set2)
# print(set1)

# print(set1.intersection(set2))

# set1.intersection_update(set2)
# print(set1)

# set1.update(set2)
# print(set1)

# s = set1.union(set2)
# print(s)
# print(set1)
# print(set2)

# set1 = {1, 2, 18, 23, 31}
# set2 = {1, 2}
#
# # print(set1.issubset(set2))
# # print(set2.issubset(set1))
#
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
