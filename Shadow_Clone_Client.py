from socket import *

host = '127.0.0.1'  # as both code is running on same pc
port = 50249  # socket server port number

client_socket = socket()  # instantiate

# txt file contains the cli interface components
#cli_style = open("style.txt", "r")
print(open("style.txt", "r").read())


# content is the string to send, choice is the option to be send to the server
def shadow_clone(content, choice):
    ''''''
    data = ''
    try:
        client_socket.connect((host, port))  # connect to the server

        choice_message = choice

        client_socket.send(choice_message.encode())  # send choice message
        client_socket.send(content.encode())  # send choice message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + str(data))  # show in terminal
        client_socket.close()  # close the connection
    except Exception as e:
        Error_msg = '''There were an error ! Please Check if you can reach the server
        Check the following for more details: \n'''
        print(Error_msg + str(e))
        input('''Press Enter to continue ...
        if you want exit type 1 and press enter''')


    return data


def main():
    run_loop = True
    while run_loop:
        choice = input('''Type 1 or 2 to run a function:-
        
        1. Function A . 
        _____________________________________________________
        
        2. Function B .
        _____________________________________________________
        
        3. Exit .
        _____________________________________________________
        
         Your Choice: ''')

        if choice == "1":
            string_to_send = shadow_clone(input("Type the string to send: "), choice)

            print('''this is choice 1
            
            ################################################################''')
        elif choice == "2":
            # send the value of a and b
            a = input("Type the value of a: ")
            b = input("Type the value of b:")

            string_to_send = shadow_clone(a + ',' + b, choice)
            print('''this is choice 2
            
            ################################################################''')
            print(string_to_send)
        elif choice == "3":
            print('''this is choice 3 Exiting !!!
            
            ################################################################''')
            client_socket.close()  # close the connection
            run_loop = False
        else:
            print(" this is invalid option! please try again !")


if __name__ == '__main__':
    main()
