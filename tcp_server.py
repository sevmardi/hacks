import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Pass ip address and port to the server we want to connect to
server.bind((bind_ip, bind_port))

# Start listining with max backlog connections of 5
server.listen(5)

print("[*] Listening on %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    # print out what the client sends
    request = client_socket.recv(1024)
    print("[*] Received: $s" % request)
    # send back a packet
    client_socket.send("ACK")
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Accepted connection from: %s:%d" (addr[0], addr[1]))
    # spin up our client thread to handle incoming data
    client_handle = threading.Thread(target=handle_client, args=(client,))
    client_handle.start()
