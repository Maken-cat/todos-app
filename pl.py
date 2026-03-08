import functions
import time

now = time.strftime("%b %d, %y - %H:%M %p")
print("It is:", now)

print("Welcome to the todos app!")
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[8:])
            index = number - 1

            todos = functions.get_todos()

            removed_todo = todos[index].strip('\n')
            todos.pop(number - 1)

            functions.write_todos(todos)
            row = f" The todo '{removed_todo}' has been removed"
            print(row)

        except IndexError or ValueError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    elif user_action.startswith("oki"):
        print()
        exit("Your not meant to know that.")

    else:
        print("invalid input")
print("Cya soon, bye!")


