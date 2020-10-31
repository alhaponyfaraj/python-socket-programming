import sys
from socket import *
from datetime import datetime
ClientSocket = socket()
host = '127.0.0.1'
port = 50249

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
            time = timer.strftime("%Y-%m-%d_%H-%M-%S")
            generated_file_name = (str(time) + "_Function_A")
            print(generated_file_name)
            data = ClientSocket.recv(1024).decode('utf-8')  # receive response
            filename = "./txt_files/file_" + generated_file_name + ".txt"
            file = open(filename, 'w')
            file_data = str(data)
            file.write(file_data)
            print('Received from server: ' + str(data))  # show in terminal

        elif choice == "2":
            timer = datetime.now()
            time = timer.strftime("%Y-%m-%d_%H-%M-%S")
            generated_file_name = (str(time) + "_Function_B")
            data = ClientSocket.recv(64024)
            filename = "./graphs/graph_" + generated_file_name + ".png"
            file = open(filename, 'wb')
            file_data = data
            file.write(file_data)
            file.close()
            print("File received successfully.")

        ClientSocket.close()  # close the connection
    except Exception as e:
        Error_msg = '''There were an error ! Please Check if you can reach the server
        Check the following for more details: \n'''
        print(Error_msg + str(e))
        exit_option = input('''\nPress Enter to continue ...
        if you want exit type 1 and press enter: ''')
        if exit_option == "1":
            ClientSocket.close()
            sys.exit()
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
            shadow_clone(input("Type the string to send: "), choice)

            print('''this is choice 1

            ################################################################''')
            ClientSocket.close()
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



            shadow_clone(a + b, choice)
            print('''this is choice 2

            ################################################################''')
            ClientSocket.close()

        elif choice == "3":
            print('''this is choice 3 Exiting !!!

            ################################################################''')
            ClientSocket.close()  # close the connection
            sys.exit()
        else:
            print(" this is invalid option! please try again !")


if __name__ == '__main__':
    main()

