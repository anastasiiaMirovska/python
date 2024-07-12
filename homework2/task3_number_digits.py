def expanded_form(number: str | int):
    number = int(number)  # Це на випадок, якщо випаде булеве значення
    number = str(number)
    numbers: list[str] = list()
    length = len(number)
    for i in range(length):
        numbers.append(number[i]+"0"*(length-i-1))
    print(" + ".join(numbers))

expanded_form(True)


# Покращена версія:
def expanded_form_better(number: str | int):
    if not isinstance(number, (int, str)):
        print("Неправильний тип даних")
        return None
    elif isinstance(number, str) and not number.isdigit():
        print("Слова не можуть бути розкладені по розрядах")
        return None
    else:
        number = int(number) # Це на випадок, якщо випаде булеве значення
        number = str(number)
        numbers: list[str] = list()
        length = len(number)
        for i in range(length):
            numbers.append(number[i]+"0"*(length-i-1))
        print(" + ".join(numbers))


expanded_form_better(True)
