import FreeSimpleGUI as sg
import ZipExtractor_backend as zb
sg.theme("Black")
lable1 = sg.Text("Select Archieve")
lable2 = sg.Text("Select destination")
input1 = sg.InputText("")
input2 = sg.InputText("")
chooseZip = sg.FileBrowse(key="zipfile")
chooseDest= sg.FolderBrowse(key="destination")
button = sg.Button("Extract")
output_label = sg.Text(key="output",text_color="green")

window = sg.Window("Archive Extractor",layout=[[lable1,input1,chooseZip],[lable2,input2,chooseDest],[button,output_label]])
event,values = window.read()
archivePath=values['zipfile']
destFolder=values['destination']
zb.extract(archivePath,destFolder)
window[output_label].update(value="Files Extracted Successfully!",text_color="green")
window.close()