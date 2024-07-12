def decor(func):
    count: int = 0

    def count_repeats():
        nonlocal count
        count += 1
        print("count: ", count)
        func()
        print("-"*20)

    return count_repeats


@decor
def func1():
    print("func1")


@decor
def func2():
    print("func1")


func1()
func1()
func2()
func1()
func1()
func2()
func1()
func1()
