task = []
vulgar_words = ['fuck', 'beat', 'bitch', 'asshole', 'poor']

while True:
    todo_list = input('Enter your Todo List Here: ').lower()

    if todo_list == '':
        print('No Empty Task is allowed...')
        continue

    if todo_list in vulgar_words:
        print('Task should not be a vulgar word...')
        continue

    if todo_list.isnumeric(): 
        print('Task should not be a number...')
        continue

    if todo_list == "exit":
        print(f'Tasks: {task}')
        break

    task.append(todo_list)
    print(f'Task added: {task}')
