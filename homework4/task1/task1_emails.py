# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)


try:
    with open("emails.txt", "r") as file:
            with open("gmails.txt", "w") as file2:
                for line in file:
                    if line.endswith("gmail.com\n"):
                        data = line.split()
                        file2.write(f"{data[-1]}\n")
except Exception as e:
    print(e)

l = "fb469d7ef430b0baf0cab6c436e70375			test@mail.ru"
