def print_list(my_list):
    str_list = []
    for i in my_list:
        str_list.append(str(i))
    output = ", ".join(str_list)
    print("Your list: ", output)


myList0 = [1, 2, 3, "Hello", True]
print_list(myList0)


def find_max(a, b, c):
    max_number = max(a, b, c)
    print("Max number: ", max_number)
    return max_number


numbers = [1, 2, 3]
print("Max number: ", find_max(*numbers))


def find_max_min(*args):
    print("Max number: ", max(args))
    return min(args)


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Min number: ", find_max_min(*my_list1))


def find_list_max(my_list):
    return max(my_list)


my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Max number in list:", find_list_max(my_list2))


def find_list_min(my_list):
    return min(my_list)


my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Min number in list: ", find_list_min(my_list3))


def create_number_from_list(my_list):
    output = ""
    for i in my_list:
        output += str(i)
    return int(output)


my_list4 = [3, 4, 5, 6, 1, 2]
print(create_number_from_list(my_list4))


def find_average(my_list):
    return sum(my_list)/len(my_list)


my_list5 = [1, 2, 3, 4, 5]
print(find_average(my_list5))
