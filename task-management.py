# name

task = []
vulgar_words = ['fuck', 'beat', 'bitch','asshole','poor' ]
todo_list = input('Enter your Todo List Here: ').lower()

while todo_list:
    if todo_list == '':
        print('No Empty Task is allowed...')
        break

    if todo_list in vulgar_words:
        print('Task should not be a vulgar word...')
        break

    if todo_list.isnumeric(): 
        print('Task should not be a number...')
        break

    if todo_list == "exit":
        task.append(todo_list)
        print(f'Task added: {task}')
        break

