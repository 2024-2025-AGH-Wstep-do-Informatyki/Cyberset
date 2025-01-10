import socket
import selectors 


ADDR = '127.0.0.1'
PORT = 34343

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((ADDR, PORT))
    print("Socket bound")
    sock.listen(1)
    print("Socket listening...")
    while(1):
        conn, addr = sock.accept()
        with conn:
            print("Connection established to: ", addr)
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("Data received from",addr,":\n", data.decode())

                except socket.error:
                    print("socket error")
                    break



if __name__ == "__main__":
    main()
