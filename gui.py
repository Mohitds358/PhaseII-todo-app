import functions
import PySimpleGUI as pg

label = pg.Text("Type in to-do app")
input_box = pg.InputText(tooltip="Enter Todo", key="todo")
add_button = pg.Button("Add")


window = pg.Window('My to-do App', layout=[[label],
                                           [input_box, add_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = "\n" + values['todo']
            todos.append(new_todo)
            functions.write_todo(todos)

window.close()

