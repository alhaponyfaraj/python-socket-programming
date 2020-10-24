from socket import *

# txt file contains the cli interface components
cli = open("style.txt", "r")
print(cli.read())

run_loop = True
while run_loop:
    choice = input('''Type 1 or 2 to run a function: ---
    1. Function A:
    2. Function B:
     Your Choice: ''')

    if choice == 1:
        print(" this is choice 1")
    elif choice == 2:
        print(" this is choice 2")
    elif choice == 3:
        print(" this is exit choice")
    else:
        print(" this is invalid option try again !")
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