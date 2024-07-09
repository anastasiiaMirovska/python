my_input = input("Введіть текст з числами:  ")
output = ""

for char in my_input:
    if not char.isnumeric():
        if len(output) == 0 or output[-1] == ",":
            continue
        else:
            output += ","
    else:
        output += char

print(output)
