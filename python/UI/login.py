import PySimpleGUI as sg


def login():
    sg.theme('SandyBeach')

    layout = [
        [sg.Text('Please enter your username and password')],
        [sg.Text('Username', size=(15, 1)), sg.InputText()],
        [sg.Text('password', size=(15, 1)), sg.InputText()],
        [sg.Submit("Login"), sg.Cancel()]
    ]

    window = sg.Window('Login screen', layout, size=(500, 300))
    event, values = window.read()
    if event == "Login":
        window.close()
        print(event, values[0], values[1])
        return event

    return False


if __name__ == "__main__":
    login()
