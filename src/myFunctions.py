import socket
def sumOfInts(num1, num2):

    return num1 + num2


def sumOfFloat(number_1, number_2):

    if isinstance(number_1, float) and isinstance(number_2, float):

        return number_1 + number_2

    else:
        raise ValueError("Both inputs must be floating point numbers")

def get_ascii_code(char):

    return ord(char)


def print_ascii_stream(sentence):
    ascii_stream = [ord(char) for char in sentence]
    for ascii_code in ascii_stream:
        print(ascii_code, end=' ')

def connect_to_google():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the target host and port
    target_host = 'www.google.com'
    target_port = 80

    # Connect to the server
    client_socket.connect((target_host, target_port))

    # Send some data
    client_socket.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

    # Receive some data
    response = client_socket.recv(4096)

    print(response.decode())

    # Close the socket
    client_socket.close()


