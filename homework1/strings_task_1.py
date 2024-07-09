my_input = input("Введіть текст з числами:  ")
numbers = []

for char in my_input:
    if char.isdecimal():
        numbers.append(char)

output = ",".join(numbers)
print(output)
