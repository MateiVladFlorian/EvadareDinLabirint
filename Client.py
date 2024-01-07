import socket

def client():
    server_ip = "127.0.0.1"
    server_port = 65438
    loops = 100

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))

    # Clientul conectat la server cu adresa ip si portul corespunzator
    # va trimite input server-ului;

    while True:
        line = input("input: ")
        client.send(line.encode("utf-8"))

        response = client.recv(104)
        response = response.decode("utf-8")

        if line.upper() == "STOP":
            break

        print(response)

    client.close()

client()
