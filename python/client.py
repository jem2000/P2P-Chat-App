# Python program to implement client side of chat room.
import socket
import select
import sys
from cryptography.fernet import Fernet
import UI.login as login
import UI.messages as messages

isWindows = sys.platform.startswith('win')
if isWindows:
    import msvcrt


def encrypt_message(fernet_suite, msg):
    return fernet_suite.encrypt(msg)


def decrypt_message(fernet_suite, msg):
    return fernet_suite.decrypt(msg).decode().strip()


args = login.login()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number, key")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
# key = sys.argv[3].encode()
# suite = Fernet(key)

# IP_address = str(args[0])
# Port = int(args[1])
# key = args[2].encode()
# suite = Fernet(key)

server.connect((IP_address, Port))

chatroom = messages.Chatroom(server)
chatroom.wait()
