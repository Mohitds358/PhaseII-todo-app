import functions
import PySimpleGUI as pg

label = pg.Text("Type in to-do app")
input_box = pg.InputText(tooltip="Enter Todo")
add_button = pg.Button("Add")


window = pg.Window('My to-do App', layout=[[label], [input_box, add_button]])
window.read()
print("this will run after you you give something in gui and add")
window.close()

