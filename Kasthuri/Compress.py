import zipfile
import zip_creator
import PySimpleGUI as sg


sg.change_look_and_feel("Dark Green")

label =sg.Text("Select file")
inputSource = sg.InputText("Select file", key="inputSource")
chooseSource = sg.FilesBrowse(key="chooseSource")

labelTarget =sg.Text("Select file")
inputTarget = sg.InputText("Select folder", key="TargetSource")
chooseTarget = sg.FolderBrowse(key="chooseTarget")

compress = sg.Button("Compress", key="Compress")

window=sg.Window("Compress",layout=[[label,inputSource,chooseSource],[labelTarget,inputTarget,chooseTarget],[compress]])
while True:
    event,values= window.read()
    print(event,values)
    filepaths= values['inputSource'].split(';')
    targetFolder = values['TargetSource']
    zip_creator.make_archieve(filepaths,targetFolder)

window.close()