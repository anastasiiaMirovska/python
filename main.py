d = {"bob": "hello", "john": "world"}
d.update({"john": "hello"})
print(d)

#l = [1, 3 , 4 , 5, 1]
# l.insert(3, 1)
# print(l)
#
# se = {1,2,9,3,8,0}
# print(se)
# se.pop()
# print(se)

l = [1,2, 3, 4, 5, 6]
a, *_, b = l
print(a, b, _)


d = {
    "name": "Bob",
    "age":18,
    "status": False
}

def test(name, age, sta):
    print(name, age, sta)

def test2(**kwargs):
    print(kwargs)

test2(**d)