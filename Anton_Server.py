from collections import defaultdict
from socket import *
import grafilio

def Anton_handshake():
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
        client_data = conn.recv(1024).decode()
        counted_string = string_counter_words(client_data)
        word_counter_letters(str(client_data))
        if not client_data and not counted_string and not word_counter_letters:
            # if data is not received break
            break
        print("from connected user: " + str(word_counter_letters(client_data)))

        server_data = str(str(word_counter_letters(client_data)))
        conn.send(server_data.encode())  # send data to the client


    conn.close()  # close the connection


def string_counter_words(string):
    print('String-', string)
    no_of_words = 1
    for ch in string:
        if (ch == ' ' or ch == '\t' or ch == '\n'):
            no_of_words += 1
    print('Total number of words in String', no_of_words)

def word_counter_letters(word):
    matches = defaultdict(int)  # makes the default value 0

    for char in word:
        matches[char] += 1

        return max(matches.items(), key=lambda x: x[1])

    word_counter_letters('helloworld')
if __name__ == '__main__':
    Anton_handshake()