import time

import PySimpleGUI as sg
from threading import Thread
import socket
import select
import sys
from queue import Queue


class Chatroom:
    def __init__(self, server):

        self.values = None
        self.event = None
        self.window = None
        self.server = server
        self.receiveQueue = Queue()
        # maintains a list of possible input streams
        self.read_sockets = [self.server]
        server_thread = Thread(target=self.read_from_server)
        server_thread.start()
        self.threads = [server_thread]
        self.runUI()

    def wait(self):
        for thread in self.threads:
            thread.join()

    def runUI(self):
        layout = [
            [sg.Text('Chatroom')],
            [sg.Frame('', [[sg.Column(layout=[], scrollable=True, key='-COL1-', size=(500, 150))]], size=(500, 150))],
            [sg.Input(key='-IN-'), sg.Text(size=(12, 1), key='-OUT-')],
            [sg.B('Send message', key='Send'), sg.Button('Exit')],
        ]

        self.window = sg.Window('Window Title', layout)
        i = 0
        while True:  # Event Loop
            self.event, self.values = self.window.read(timeout=100)
            # print(self.event, self.values)
            if self.event in (sg.WIN_CLOSED, 'Exit'):
                break
            if self.event == 'Send':
                self.window.extend_layout(self.window['-COL1-'], [[sg.T(
                    '                                            ' + self.values['-IN-'])]])
                self.write_to_server(self.values['-IN-'])
            i += 1
            try:
                message = self.receiveQueue.get_nowait()
            except Exception:
                message = ""

            if message != '':
                self.add_message(message)
            self.window.Refresh()
            # self.add_message(str(i))
            self.window['-COL1-'].contents_changed()

        self.window.close()

    def add_message(self, msg):
        self.window.extend_layout(self.window['-COL1-'], [[sg.T(msg)]])

    def read_from_server(self):
        while True:
            ready, _, _ = select.select(self.read_sockets, [], [])
            for sock in ready:
                if sock == self.server:
                    message = sock.recv(2048)
                    print("From Server: ", message)
                    self.receiveQueue.put(message)
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
    c = Chatroom()
    c.wait()

