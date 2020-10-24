from socket import *

# txt file contains the cli interface components
cli = open("style.txt", "r")
print(cli.read())

choice_1 = input("Type 1 to run function A: ")
choice_2 = input("Type 2 to run function B: ")

def shadow_clone():
    host = '127.0.0.1' # as both code is running on same pc
    port = 50249  # socket server port number

    client_socket = socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    ''''''
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + str(data))  # show in terminal

        message = input(" -> ")  # again take input

    #lient_socket.close()  # close the connection

if __name__ == '__main__':
    shadow_clone()