import functions
import PySimpleGUI as pg

label = pg.Text("Type in to-do app")
input_box = pg.InputText(tooltip="Enter Todo", key="todo")
add_button = pg.Button("Add")
list_box = pg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[44,10])
edit_button = pg.Button("Edit")
complete_button = pg.Button("Complete")
exit_button = pg.Button("Exit")

window = pg.Window('My to-do App',
                   layout=[[label],
                   [input_box, add_button],
                   [list_box, edit_button, complete_button],
                   [exit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            completed_todo = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(completed_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case pg.WIN_CLOSED:
            break

window.close()

