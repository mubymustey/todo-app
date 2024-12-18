#pypi.org has a complete list of python third party libraries
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do") #all these are widgets created
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()  #displays it
window.close() #closes it