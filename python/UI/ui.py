import login
import contact_list
import messages
import PySimpleGUI as sg

if __name__ == "__main__":
    window = sg.Window('Login screen', [], size=(1000, 300))
    logged_in = login.login()
    if logged_in:
        chosen_contact = contact_list.home()
        if chosen_contact is not None:
            messages.view_messages()

