while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt','r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index+1}-{item}")
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos[number] = input('Enter a new todo: ') + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
print('bye')