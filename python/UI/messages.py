import PySimpleGUI as sg

help(sg.Column)

messages = ['hi', 'r'], ['hello', 's'], ['how are you doing?', 'r'],\
           ['good! This is a super interesting conversation', 's'], \
           ['Let\'s restart then', 'r'], \
           ['hi', 'r'], ['hello', 's'], ['how are you doing?', 'r']



def view_messages():
    column = []
    for message in messages:
        if message[1] == 'r':
            column.append([sg.Text(message[0])])
            # column.append(['', message[0]])
        elif message[1] == 's':
            column.append([sg.Text('                                            ' + message[0])])

    layout = [
        [
            sg.Column(column, scrollable=True, size=(500, 100)),
        ],
        [sg.Text('')], [sg.Text('')], [sg.Text('')], [sg.Text('')],
        [sg.Text('Send message')],
        [sg.Text('Aa', size=(15, 1)), sg.InputText()]

    ]

    window = sg.Window('messages', layout, size=(500, 300))
    event, values = window.read()
    window.close()


if __name__ == "__main__":
    view_messages()
