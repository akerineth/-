import PySimpleGUI as sg
import katefunc as kt
import os
import random as rd
from PIL import Image
from io import BytesIO


def convertToPNG(path):
    im1 = Image.open(path)
    new_path = path.split(".")[0] + ".png"
    im1.save(new_path)
    return new_path

def katya(path):
    im1 = Image.open(path)
    new_path = os.getcwd() + r"\tmp\\" + str(rd.randint(1, 10000000000)) + ".png"
    im1.save(new_path)
    return new_path

katya(r"D:\train\112445.jpg")
# Define the window's contents
left = [[sg.Text("Path")],
          [sg.Input(key='-INPUT1-')],
          [sg.Input(key="-INPUT2-")],
          [sg.Input(key="-INPUT3-")],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ]]

right = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

layout = [[sg.Column(left),
          sg.VSeparator(),
          sg.Column(right)]
         ]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    path = values["-INPUT1-"]
    path1 = path + "\\"
    obj = list(map(int, values["-INPUT2-"].split(" ")))
    conf = float(values["-INPUT3-"])
    if event == "Ok":
        files = (kt.main_cycle(path, obj, conf))
        window["-FILE LIST-"].update(files)
    if event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                path1, values["-FILE LIST-"][0][0]
            )
            #filename = convertToPNG(filename)
            #print(files[0][0])
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)

        except:
            print("ASHIPKA")
            pass




#print(path, obj)
# Finish up by removing from the screen
window.close()