#Генератори

# def generator1(n):
#     for i in range(1,n+1):
#         yield f"{i} - Team1"
#
# def generator2(n):
#     for i in range(1,n+1):
#         yield f"{i} - Team2"
#
#
# teams = [generator1(5), generator2(8)]
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

import uuid


def generate_file_name():
    pattern = "{}.jpg"
    count = 0
    while True:
        yield pattern.format(f"{uuid.uuid1()}{count}")
        count += 1

filename = generate_file_name()

try:
    with open("image.jpg", "rb") as file1:
        image = file1.read()
        for _ in range(5):
            with open(next(filename), "wb") as file:
                file.write(image)

except Exception as error:
    print(error)