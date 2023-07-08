import socket

# client end of socket, will receive strings

# put into a function and change where the data goes
HOST = "127.0.0.1" 
PORT = 65422 


# to be updated based on what command is entered into command line
#   ex) command: clothingGenerate -> set var option == 1
#   ex) command: accessoryGenerate -> set var option == 0
option = 1

## make a function for this and call it/update the option variable depending on given command
## creates socket object, connect() to server, calls sendall()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    ## b - bites
    if option == 0:
        s.sendall(b"0")    
    elif option == 1:
        s.sendall(b"1")   
    data = s.recv(1024)
    data = data.decode()

## reads server reply-> print
# currently goes to screen w/print, put in variable and go from there
print(f"{data}")

