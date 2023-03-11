while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                print(f"{index+1}-{item}")
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number = number - 1
            todos[number] = input('Enter a new todo: ')
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
print('bye')