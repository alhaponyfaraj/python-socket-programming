
from collections import defaultdict, Counter
from socket import *
from grafilio import draw_graph, r_cos
from _thread import *
import os

ServerSocket = socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    try:
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            client_data = connection.recv(1024)
            choice = client_data.decode()[0]
            print("hey")

            # Run
            if choice == "1":
                client_data_string = client_data.decode()[1:]
                print(choice, client_data_string)
                server_data = str(word_letter_count(client_data_string))

                connection.send(server_data.encode())  # send data to the client

            if choice == "2":

                c = client_data.decode('utf-8')
                client_data_string = c[1:]
                a = float((c[1]))
                b = float(c[2])
                draw_graph(r_cos(a, b))
                result = open("temp.png", "rb").read(8128)


                #print(a , b)
                #print(choice, client_data_string)

                #server_data = str(word_letter_count(client_data_string))
                connection.send(result)  # send data to the client

            if not client_data and not client_data_string:
                # if data is not received break
                break
    except Exception as e:
        print(str(e))



def word_letter_count(str):
    word_counts = dict()
    letter_counts = dict()
    words = str.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        letters = word.split()
        for letter in word:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    counter = Counter(word_counts)

    counter2 = Counter(letter_counts)
    most_occur_word = counter.most_common(1)
    most_occur_letter = counter2.most_common(1)
    return most_occur_letter, most_occur_word

def plot_graph(a, b):
    draw_graph(r_cos(a, b))

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()