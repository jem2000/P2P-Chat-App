# Python program to implement client side of chat room.
import socket
import select
import sys
from cryptography.fernet import Fernet


def encrypt_message(suite, message):
    return suite.encrypt(message)
    # return message

def decrypt_message(suite, message):
    return suite.decrypt(message).decode().strip()

isWindows = sys.platform.startswith('win')
if isWindows:
    import msvcrt

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 4:
    print("Correct usage: script, IP address, port number, key")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
key = sys.argv[3].encode()
suite = Fernet(key)
server.connect((IP_address, Port))

while True:

    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]

    """ There are two possible input situations. Either the
    user wants to give manual input to send to other people,
    or the server is sending a message to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    
    # Get the list sockets which are readable, time-out after 1 s
    if isWindows:
        read_sockets = select.select([server], [], [], 1)[0]
        if msvcrt.kbhit():
            read_sockets.append(sys.stdin)
    else:
        read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            try:
                encrypted = message.decode().split(" ")[1]
                print("Encrypted:", encrypted.encode())
                print("Decrypted: ", decrypt_message(suite, encrypted.encode()))
            except Exception as err:
                print(err)
                print("From Server: ", message)
        else:
            message = sys.stdin.readline()
            server.send(encrypt_message(suite, message.encode()))
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
