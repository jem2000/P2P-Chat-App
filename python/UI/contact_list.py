import PySimpleGUI as sg

my_contacts = ['Damon', 'Damien', 'Darius']


def home():
    layout = []
    for contact in my_contacts:
        layout.append([sg.Button(contact)])
    window = sg.Window("Contacts list", layout, size=(500, 300))
    event, values = window.read()
    if event in my_contacts:
        window.close()
        return True


if __name__ == "__main__":
    home()
