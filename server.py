import socket
import selectors


ADDR = '127.0.0.1'
PORT = 34347
sel = selectors.DefaultSelector()


def accept(sock):
    conn, addr = sock.accept()
    print("Connection established to:",addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, lambda conn: handleClient(conn,addr))

def handleClient(conn,addr):
    try: 
        data = conn.recv(1024)
        if data:
            print("Data received from client:", data.decode())
        else:
            print("Closing connection to",addr)
            sel.unregister(conn)
            conn.close()
    except socket.error as e:
        print("socket error: ", e)
        sel.unregister()
        conn.close()




def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((ADDR, PORT))
    print("Socket bound")
    sock.listen(1)
    print("Socket listening...")
    sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, accept)
    try:
        while True:
            events = sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        sel.close()


if __name__ == "__main__":
    main()
