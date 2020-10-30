import socket, sys
from datetime import datetime
ClientSocket = socket.socket()
import matplotlib.pyplot as plt
host = '127.0.0.1'
port = 1233

print('Waiting for connection')

# txt file contains the cli interface components
# cli_style = open("style.txt", "r")
print(open("style.txt", "r").read())


# content is the string to send, choice is the option to be send to the server
def shadow_clone(content, choice):
    ''''''

    data = ''
    try:
        ClientSocket.connect((host, port))  # connect to the server

        choice_message = choice

        ClientSocket.send(choice_message.encode())  # send choice message
        ClientSocket.send(content.encode())  # send choice message

        # Decide which function to run

        if choice == "1":
            timer = datetime.now()
            time = timer.strftime("%Y-%m-%d_%H:%M:%S")
            generated_file_name = (str(time) + "-Function_A.txt")
            print(generated_file_name)
            data = ClientSocket.recv(1024).decode()  # receive response
            print('Received from server: ' + str(data))  # show in terminal
            ClientSocket.close()
        elif choice == "2":
            timer = datetime.now()
            time = timer.strftime("%Y-%m-%d_%H:%M:%S")
            generated_file_name = (str(time) + "-Function_B")
            data = ClientSocket.recv(8128)
            filename = generated_file_name + ".png"
            file = open(filename, 'wb')
            file_data = data
            file.write(file_data)
            file.close()
            print("File has been received successfully.")

            #data = ClientSocket.recv(1024).decode()  # receive response
            #print('Received from server: ' + str(data))  # show in terminal
            #plot_data = data
            #plt.show(plot_data)
        #ClientSocket.close()  # close the connection
    except Exception as e:
        Error_msg = '''There were an error ! Please Check if you can reach the server
        Check the following for more details: \n'''
        print(Error_msg + str(e))
        exit_option = input('''\nPress Enter to continue ...
        if you want exit type 1 and press enter: ''')
        if exit_option == "1":
            sys.exit()
    #ClientSocket.close()
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
            a = input("Type the value of a:")
            # Set a loop to set the right value for a and b
            a_condition = True
            while a_condition:
                if int(a) > 10 or int(a) < 0:
                    print("This is an invalid number")
                    a = input("Type the value of a:")
                else:
                    a_condition = False

            b = input("Type the value of b:")
            b_condition = True
            while b_condition:

                if int(b) > 10 or int(b) < 0:
                    print("This is an invalid number")
                    b = input("Type the value of b:")
                else:
                    b_condition = False



            string_to_send = shadow_clone(a + b, choice)
            print('''this is choice 2

            ################################################################''')
            print(string_to_send)
        elif choice == "3":
            print('''this is choice 3 Exiting !!!

            ################################################################''')
            ClientSocket.close()  # close the connection
            sys.exit()
        else:
            print(" this is invalid option! please try again !")


if __name__ == '__main__':
    main()
