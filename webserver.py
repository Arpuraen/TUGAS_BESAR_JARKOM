from socket import *    # Mengimport modul socket
import sys              # Mengimport sys yang berguna untuk menghentikan program
import os

# Membuat TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)     # Membuat socet TCP dengan memanggil fungsi socket dan disimpan di variabel serverSocket
serverPort = 8080  # Nomor port
serverSocket.bind(('', serverPort))  # Mengikat port ke soket
serverSocket.listen(1)  # Menunggu request
print("Ready to serve . . .")

# Dictionary mapping file extensions to content types
content_types = {
    "html": "text/html",
    "css" : "text/css"
}

while True:
    connectionSocket, addr = serverSocket.accept()  # Membuat soket koneksi dan menerima request

    try:        # Mencoba menjalankan code yang berguna untuk mencari dan mengambil file dari file system
        # Menerima message dan mencari file yang diminta
        message = connectionSocket.recv(1024).decode() # Memasukkan paket ke yang sudah tiba kedalam variabel message dan mengkonversikan paketnya dari byte ke tipe data yang normal
        filename = message.split()[1]                  # Memasukkan value dengan indeks ke 1 dari message yang sudah displit kedalam variabel filename
        f = open(filename[1:], 'rb')                   # Open file in binary mode for images
        outputdata = f.read()                          # Membaca konten dari file f ke variabel outputdata

        print("File found.")
        # Membuat header bahwa file telah ditemukan dan mengirim file
        extension = os.path.splitext(filename)[1][1:].lower()
        content_type = content_types.get(extension, "application/octet-stream")
        header = "HTTP/1.1 200 OK\r\nContent-Type: {}\r\n\r\n".format(content_type)
        response = header.encode()+outputdata
        connectionSocket.send(response)

        # Memutuskan koneksi
        print("File sent.")
        connectionSocket.close()        # Menutup koneksi soket connectionSocket

    except IOError:     # Menjalankan code jika codingan pada blok try error (jika file tidak ditemukan)
        # Membuat header error
        error = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response1 = error.encode()
        connectionSocket.send(response1)

        # Mencari file error dan mengirim file error
        ferr = open("404.html", 'r')
        outputerr = ferr.read()
        ferr.close()

        # Memutuskan koneksi
        print("Error message sent.")
        connectionSocket.close()        # Menutup koneksi soket ConnectionSocket

# Tutup aplikasi
serverSocket.close()    # Menutup koneksi soket serverSocket
sys.exit()              # Mengakhiri program dengan metode exit()
