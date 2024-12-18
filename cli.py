# dir (str)
# help (str.capitalize)
# str.title (capitalize the first letter of each words)
# str.capitalize (capitalizes the first letter of the first word alone)
# case 'add' | 'another'
# mylist.__setitem__(1, 'a'). Note that it's used by python internally. mylist[1] = 'a'
# mylist.__getitem__(1). Note that it's used by python internally. mylist[1]
# since string is immutable, this is how to change a variable. filename.replace('.', '-', 1). The last number specifies the position wanted
#a = enumerate('Mubarak'). won't show until you use list(a)
# take note of this code
# for content, filename in zip(contents, filenames):
#     file = open(f"../files/{filename}", 'w')
#     file.write(content)
# custom functions are created outside your code
#from functions import get_todos, write_todos

# ensure you use docs.python.org

import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos) #we removed todos.txt as we've made the file path default

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        number = int(user_action[9:])

        todos = functions.get_todos()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        functions.write_todos(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)


    elif 'exit' in user_action:
            break
    else:
        print("Command is not valid.")

print("Bye!")