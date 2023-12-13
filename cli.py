"""Day 1

user_prompt = "Enter a todo:"

todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)

print(type(user_prompt))
print(type(todos))"""

"""Day 2
user_prompt = "Enter a todo: "
todos = []
while True:
    todo = input(user_prompt)
    todos.append(todo)
    ask_opinion = input("Do you want to add more todos Y/N: ").upper()
    if ask_opinion == 'N':
        break

print(todos)"""

"""Day 3
todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Tata!")"""

"""Day 4 + Day 5
todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for num,item in enumerate(todos):
                print(f"{num+1}. {item}")
        case 'edit':
            if len(todos) > 0:
                editing = int(input("Which todo item number you want to edit: "))
                editing -= 1
                edited = input("What you want to change it to: ")
                todos[editing] = edited
            else:
                print("Add some item")
        case 'complete':
            if len(todos) > 0:
                completed = int(input("Which todo item number is completed: "))
                todos.pop(completed - 1)
            else:
                print("Add some item")
        case 'exit':
            break

print("Tata!")"""

"""Day 6 and Day 7

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = [item.strip("\n") for item in todos]

            for num,item in enumerate(new_todos):
                item = item.strip('/n')            
                print(f"{num+1}. {item}")
        case 'edit':
            if len(todos) > 0:
                editing = int(input("Which todo item number you want to edit: "))
                editing -= 1
                edited = input("What you want to change it to: ")
                todos[editing] = edited
            else:
                print("Add some item")
        case 'complete':
            if len(todos) > 0:
                completed = int(input("Which todo item number is completed: "))
                todos.pop(completed - 1)
            else:
                print("Add some item")
        case 'exit':
            break

print("Tata!")"""

"""Day 8

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip("\n") for item in todos]

            for num,item in enumerate(todos):
                item = item.strip('\n')
                print(f"{num+1}. {item}")
        case 'edit':
            if len(todos) <= 0:
                print("Add some item")
            else:
                editing = int(input("Which todo item number you want to edit: "))
                editing -= 1

                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                edited = input("What you want to change it to: ")
                todos[editing] = edited

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
        case 'complete':
            if len(todos) <= 0:
                print("Add some item")
            else:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                completed = int(input("Which todo item number is completed: "))
                index = completed - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                message = f"Removed Todo is {todo_to_remove}"
                print(message)
        case 'exit':
            break

print("Tata!")"""

"""Day 9 and Day 10

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        if todos and not todos[-1].endswith('\n'):
            todos[-1] = todos[-1] + '\n'

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip("\n") for item in todos]

        for num, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{num+1}. {item}")
    elif user_action.startswith('edit'):
        try:
            if len(todos) > 0:
                editing = int(user_action[5:])
                editing -= 1

                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                edited = input("What you want to change it to: ")
                todos[editing] = edited

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            else:
                print("Add some item")
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            if len(todos) > 0:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()

                completed = int(user_action[9:])
                index = completed - 1
                todo_to_remove = todos[index].strip('\n')
                todos.pop(index)

                with open('todos.txt', 'w') as file:
                    file.writelines(todos)

                message = f"Removed Todo is {todo_to_remove}"
                print(message)
            else:
                print("Add some item")
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Chose Wrong Option!")

print("Tata!")"""

"""Day 11 & Day 12


def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos('todos.txt')

        if todos and not todos[-1].endswith('\n'):
            todos[-1] = todos[-1] + '\n'

        todos.append(todo)

        write_todo('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = get_todos('todos.txt')

        # new_todos = [item.strip("\n") for item in todos]

        for num, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{num + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            editing = int(user_action[5:])
            editing -= 1

            todos = get_todos('todos.txt')

            edited = input("What you want to change it to: ")
            todos[editing] = edited

            write_todo('todos.txt', todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos('todos.txt')

            completed = int(user_action[9:])
            index = completed - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todo('todos.txt', todos)

            message = f"Removed Todo is {todo_to_remove}"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Chose Wrong Option!")

print("Tata!")"""

"""Day 13


def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        if todos and not todos[-1].endswith('\n'):
            todos[-1] = todos[-1] + '\n'

        todos.append(todo)

        write_todo(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for num, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{num + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            editing = int(user_action[5:])
            editing -= 1

            todos = get_todos()

            edited = input("What you want to change it to: ")
            todos[editing] = edited

            write_todo(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            completed = int(user_action[9:])
            index = completed - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todo(todos)

            message = f"Removed Todo is {todo_to_remove}"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Chose Wrong Option!")

print("Tata!")"""

"""Day 14 """

from functions import get_todos, write_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        if todos and not todos[-1].endswith('\n'):
            todos[-1] = todos[-1] + '\n'

        todos.append(todo)

        write_todo(todos)

    elif user_action.startswith('show'):
        todos = get_todos()

        # new_todos = [item.strip("\n") for item in todos]

        for num, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{num + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            editing = int(user_action[5:])
            editing -= 1

            todos = get_todos()

            edited = input("What you want to change it to: ")
            todos[editing] = edited

            write_todo(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            completed = int(user_action[9:])
            index = completed - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todo(todos)

            message = f"Removed Todo is {todo_to_remove}"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Chose Wrong Option!")

print("Tata!")
