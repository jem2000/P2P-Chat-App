import login
import contact_list
import messages
import PySimpleGUI as sg

if __name__ == "__main__":
    open_chat = login.login()
    if open_chat:
        messages.view_messages()
    # logged_in = login.login()
    # if logged_in:
    #     chosen_contact = contact_list.home()
    #     if chosen_contact is not None:
    #         messages.view_messages()

