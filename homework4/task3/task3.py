data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]


def go_through(my_data):
    for item in my_data:
        yield item["id"]


g1 = go_through(data[0])
g2 = go_through(data[1])
g3 = go_through(data[2])

list = [g1, g2, g3]
res = []

while list:

    item = list.pop(0)
    try:
        proceed = True
        while proceed:
            element = next(item)
            if element in res:
                continue
            else:
                res.append(element)
                list.append(item)
                proceed = False

    except StopIteration:
        pass

print(res)
