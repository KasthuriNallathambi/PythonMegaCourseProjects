from asyncio import events

import PySimpleGUI as gui
import function
import time
import os

if not os.path.exists('TodoList.txt'):
    with open('TodoList.txt','w') as file:
        pass

label=gui.Text("Enter Todo")
NewTodo = gui.InputText(tooltip="Enter the todo to add in the list",key="NewTodo")
listItems = gui.Listbox(key="TodoList",values=function.get_todos(),size=[50,10],enable_events=True)
addButton =gui.Button("Add")
EditButton =gui.Button("Edit")
CompleteButton =gui.Button("Complete")
clock = gui.Text(key="Clock")
gui.theme("Dark Blue")
window = gui.Window(title="My Todo App",layout=[[clock],
        [NewTodo,addButton],
    [listItems,EditButton],[CompleteButton]
])

while True:
    Event,values = window.read(timeout=10)
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(Event,values)
    match Event:
        case "Add":

            todo_list = function.get_todos()
            NewTodo = values['NewTodo']+'\n'
            todo_list.append(NewTodo)
            window["TodoList"].update(values=todo_list)
            window["NewTodo"].update(value="")

        case "Edit":
            try:
                tobeEdited = values['TodoList'][0]
                new_todo = values['NewTodo']
                todo_list = function.get_todos()
                index = todo_list.index(tobeEdited)
                todo_list[index] = new_todo
                function.write_todos(todo_list)
                window["TodoList"].update(values=todo_list)
                window["NewTodo"].update(value="")
            except IndexError:
                gui.popup("Select the todo to edit")
        case "TodoList":
            window["NewTodo"].update(value=values["TodoList"][0])
        case "Complete":
            try:
                window["NewTodo"].update(value=values["TodoList"][0])
                todo_over = values['TodoList'][0]
                todo_list = function.get_todos()
                todo_list.remove(todo_over)
                function.write_todos(todo_list)
                window["TodoList"].update(values=todo_list)
                window["NewTodo"].update(value="")
            except IndexError:
                gui.popup("Select the todo to edit")
        case "Exit":
            gui.popup("Goodbye")
window.close()

