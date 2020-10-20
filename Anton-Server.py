from socket import *

def server_program():
    # get the hostname
    host = '127.0.0.1'
    port = 50249  # initiate port no above 1024

    server_socket = socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        counted_sting = string_counter(data)
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))

        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
        conn.send(counted_sting.encode())

    conn.close()  # close the connection


def string_counter(string):
    print('String-', string)
    no_of_words = 1
    for ch in string:
        if (ch == ' ' or ch == '\t' or ch == '\n'):
            no_of_words += 1
    print('Total number of words in String', no_of_words)

if __name__ == '__main__':
    server_program()