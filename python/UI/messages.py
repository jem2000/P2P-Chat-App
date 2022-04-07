import time

import PySimpleGUI as sg
from threading import Thread
import socket
import select
import sys


def wait():
    print("starting")
    time.sleep(5)


class Chatroom:
    def __init__(self, server):
        self.server = server
        # maintains a list of possible input streams
        sockets_list = [self.server]
        self.read_sockets, _, _ = select.select(sockets_list, [], [])

        layout = [
            [sg.Text('Chatroom')],
            [sg.Frame('', [[sg.Column(layout=[], scrollable=True, key='-COL1-', size=(500, 150))]], size=(500, 150))],
            [sg.Input(key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
            [sg.B('Send message', key='Send'), sg.Button('Exit')],
        ]

        self.window = sg.Window('Window Title', layout)
        i = 0
        while True:  # Event Loop
            self.event, self.values = self.window.read(timeout=1000)
            # print(self.event, self.values)
            if self.event in (sg.WIN_CLOSED, 'Exit'):
                break
            if self.event == 'Send':
                self.window.extend_layout(self.window['-COL1-'], [[sg.T(
                    '                                            ' + self.values['-IN-'])]])
                self.write_to_server(self.values['-IN-'])
            i += 1
            message = self.read_from_server()
            if message != '':
                self.add_message(message)
            self.window.Refresh()
            # self.add_message(str(i))
            self.window['-COL1-'].contents_changed()

        self.window.close()

    def add_message(self, msg):
        self.window.extend_layout(self.window['-COL1-'], [[sg.T(msg)]])

    def read_from_server(self):

        for socks in self.read_sockets:
            if socks == self.server:
                ready = select.select([socks], [], [], 0.2)
                if ready[0]:
                    message = socks.recv(2048)
                    print("From Server: ", message)
                    return message
        return ''
        # try:
        #     encrypted = message.decode().split(" ")[1]
        #     print("Encrypted:", encrypted.encode())
        #     print("Decrypted: ", decrypt_message(suite, encrypted.encode()))
        # except Exception as err:
        #     print(err)
        #     print("From Server: ", message)
        #     else:
        #         message = sys.stdin.readline()
        #         self.server.send(message.encode())
        #         # server.send(encrypt_message(suite, message.encode()))
        #         sys.stdout.write("<You>")
        #         sys.stdout.write(message)
        #         sys.stdout.flush()
        # self.server.close()

    def write_to_server(self, msg):
        self.server.send(msg.encode())
        # server.send(encrypt_message(suite, message.encode()))
        sys.stdout.write("<You>")
        sys.stdout.write(msg)
        sys.stdout.flush()

if __name__ == "__main__":
    Chatroom()
