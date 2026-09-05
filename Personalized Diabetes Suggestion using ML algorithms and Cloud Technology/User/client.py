









import socket
import cv2

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    diet = ""

    filedata = ""
    with open("users.txt", "r", errors='ignore') as file:
       for line in file:
          line = line.strip('\n')
          filedata+=line+" "

    with open("img/plan.txt", "r", errors='ignore') as file:
       for line in file:
          diet+=line+" "
          
    file = filedata.split(" ")
    length = len(file)
    print(length)
    i = 0
    j = 0
    while i < length:
       client_socket = socket.socket()  # instantiate
       client_socket.connect((host, port))  # connect to the server
       message = str(file[i])
       print(message)
       client_socket.send(message.encode())  # send message
       data = client_socket.recv(1024).decode()  # receive response
       print('Received from server: ' + data)  # show in terminal
       client_socket.close()
       if j == 0 and data == 'Abnormal Values. Disease predicted as type 2 diabetes':
           img = cv2.imread("img/1.jpg");
           cv2.imshow(img)
           
       i = i + 1

         #message = input(" -> ")  # again take input
    print("ended")
    client_socket.close()  # close the connection
    print("ended")

if __name__ == '__main__':
    client_program()
