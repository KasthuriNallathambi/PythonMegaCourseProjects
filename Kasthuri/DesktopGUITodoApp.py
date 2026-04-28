from asyncio import events

import FreeSimpleGUI as gui
import function

label=gui.Text("Enter Todo")
NewTodo = gui.InputText(tooltip="Enter the todo to add in the list",key="NewTodo")
listItems = gui.Listbox(key="TodoList",values=function.get_todos(),size=[50,10])
addButton =gui.Button("Add")
EditButton =gui.Button("Edit")
CompleteButton =gui.Button("Complete")

window = gui.Window(title="My Todo App",layout=[
        [NewTodo,addButton],
    [listItems,EditButton],[CompleteButton]
])


Event,values = window.read()
print(Event,values)
window.close()

