from socket import *

host = '127.0.0.1'  # as both code is running on same pc
port = 50249  # socket server port number

client_socket = socket()  # instantiate
client_socket.connect((host, port))  # connect to the server

# txt file contains the cli interface components
#cli_style = open("style.txt", "r")
print(open("style.txt", "r").read())


# content is the string to send, choice is the option to be send to the server
def shadow_clone(content, choice):
    ''''''
    choice_message = choice

    client_socket.send(choice_message.encode())  # send choice message
    client_socket.send(content.encode())  # send choice message
    data = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + str(data))  # show in terminal

    return data


def main():
    run_loop = True
    while run_loop:
        choice = input('''Type 1 or 2 to run a function: ---
        1. Function A . 
        2. Function B .
        3. Exit .
         Your Choice: ''')

        if choice == "1":
            string_to_send = shadow_clone(input("Type the string to send: "), choice)

            print(" this is choice 1")
        elif choice == "2":
            a = input("Type the value of a: ")
            b = input("Type the value of b:")
            print(a +','+ b)
            string_to_send = shadow_clone(a +',' + b, choice)
            print(" this is choice 2")
            print(string_to_send)
        elif choice == "3":
            print(" this is exit choice")
            client_socket.close()  # close the connection
            run_loop = False
        else:
            print(" this is invalid option! please try again !")


if __name__ == '__main__':
    main()
