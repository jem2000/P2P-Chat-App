import PySimpleGUI as sg


def login():
    sg.theme('SandyBeach')

    layout = [
        [sg.Text('')],
        [sg.Text('Open the chatroom using IP, port, and encryption key')],
        [sg.Text('')],
        [sg.Text('IP address', size=(15, 1)), sg.InputText()],
        [sg.Text('Port', size=(15, 1)), sg.InputText()],
        [sg.Text('key', size=(15, 1)), sg.InputText()],
        [sg.Text('')], [sg.Text('')], [sg.Text('')],

        [sg.Submit("Open Chatroom"), sg.Cancel()]
    ]

    window = sg.Window('Login screen', layout, size=(500, 300))
    event, values = window.read()
    if event == "Open Chatroom":
        window.close()
        print(event, values[0], values[1], values[2])
        return values

    return False


if __name__ == "__main__":
    login()
