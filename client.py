import socket
import selectors

HOST = "127.0.0.1"
PORT = 34343


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST,PORT))
        print("Connection established to: ",HOST)
    except socket.error:
        print("Couldn't connect to the server")

    while(1):
        try:
            data = input("Enter text that will be forwarded to server:\n")
            sock.sendall(data.encode())
        except  socket.error:
            print("socket error")
            break
            

if __name__ == "__main__":
            main()
