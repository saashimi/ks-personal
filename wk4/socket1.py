import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = raw_input("Type in a url. >> ")
mysock.connect((url, 80))
mysock.send('GET http://' + url + " HTTP/1.0\n\n")

count = 0
while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    count = count + len(data)
    print data
print len(data), count

mysock.close()