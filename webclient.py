import socket

# Membuat TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Menentukan alamat server dan nomor port
serverAddress = ('localhost', 8080)

# Melakukan koneksi ke server
clientSocket.connect(serverAddress)

try:
    # Mengirimkan request ke server
    request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
    clientSocket.sendall(request.encode())

    # Menerima response dari server
    response = clientSocket.recv(4096).decode()

    # Mencetak response
    print(response)

finally:
    # Menutup koneksi
    clientSocket.close()
