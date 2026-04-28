import PySimpleGUI as sg

feet_label=sg.Text("Enter Feet")
feet=sg.InputText(tooltip="Enter Feet",key="feet")

inches_label=sg.Text("Enter inches")
inch=sg.InputText(tooltip="Enter inches",key="inch")

covert = sg.Button("Convert",key="Convert",size=10)
exitButton = sg.Button("Exit",key="ExitButton",size=10)

output = sg.Text(key="output",size=(10),justification="center")

window = sg.Window("Converter",[[feet_label,feet],[inches_label,inch],[covert,exitButton,output]], finalize=True)



while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
         try:
          feet_value =float(values["feet"])
          inch_value=float(values["inch"])
          result = feet_value*inch_value
          print(f"result is {result}")
          window["output"].update(value=f"{result}m")
         except ValueError:
          sg.Popup("Please enter a numeric value")
        case "ExitButton":
          break
        case WIN_ClOSED:
          break
window.close()


