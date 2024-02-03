# reference: https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
import socket
def run_server(): 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO: move to a config file later
    server_ip = "127.0.0.1"
    port = 8000
    server.bind((server_ip, port))
    server.listen(0)
    print(f"INFO: Listening on {server_ip}:{port}")
    client_socket, client_address = server.accept()
    print(f"INFO: Accepted connection from {client_address[0]}:{client_address[1]}")

    # communication loop
    while True: 
        request = client_socket.recv(1024)
        request = request.decode("utf-8")

        if request.lower() == "close":
            client_socket.send("closed".encode("utf-8"))
            break

        print(f"INFO: Received: {request}")
        response = "accepted".encode("utf-8")
        client_socket.send(response)
    client_socket.close()
    print("INFO: Connection to client closed")
    server.close()

run_server()
