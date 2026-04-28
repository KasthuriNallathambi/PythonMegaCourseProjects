import PySimpleGUI as sg

sg.change_look_and_feel("Dark Green")

label =sg.Text("Select file")
chooseSource = sg.FileBrowse()

window=sg.Window("Compress",layout=[[label,chooseSource]])
window.read()
window.close()