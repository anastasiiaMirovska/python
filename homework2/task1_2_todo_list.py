def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


add_todo1, get_all1 = notebook()
add_todo1("Зробити домашнє завдання")
add_todo1("Написати python програму")
add_todo1("Відпочити")
print(get_all1())