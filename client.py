import socket

def run_client(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # TODO replace with config file values
    server_ip = "127.0.0.1"
    server_port = 8000
    client.connect((server_ip, server_port))

    # communication loop 
    try:
        while True: 
            msg = input("Enter message: ")
            client.send(msg.encode("utf-8")[:1024])
            response = client.recv(1024)
            response = response.decode("utf-8")
            if response.lower() == "closed": 
                break
            print(f"INFO: Received: {response}")
    except Exception as e:
        print(f"DEBUG: Error {e}")
    finally: 
        client.close()
    print("INFO: Connection to server closed")

run_client()
