import socket
import random
import time

## loopback|localhost
HOST = "127.0.0.1"  

## TCP port for clients
PORT = 65422  

## FORMAT for passing messages
FORMAT = 'utf-8'



# Important: resets connection so server can receieve multiple client requests without stalling
while True:

    ## Create a socket object
    ## Address family|AF_INET(internet) & SOCK_STREAM|TCP sock type(transport prot)
    ## with- file streams || used w/conn object in closing socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        ## console message

        ## .bind association with network interface & port
        s.bind((HOST, PORT))

        ## makes listening socket
        s.listen()

        ## accept blocks execution& waits for connection & tup w/address of client (looks like it's hanging initially)
        ## accept is a new socket object - used to communicate with client (diff from listening socket for new connections)
        ## conn - socket object || addr - information about connection
        conn, addr = s.accept()

        ## conn- socket object
        with conn:
            print(f"Connected to client at {addr}.")
            ## loop over blocking calls to conn.recv() - reads from client and echos back using sendall()
            # try to reset
            connectionSet = True
            while connectionSet:
                message = conn.recv(1024)
                time.sleep(1)
                message = message.decode()

                occasion = ['appropriate','very inappropriate','apt','strange']
                color = ['red','blue','yellow','orange','green','red','purple','brown','white','black','pink']
                clothing = ['shirt','pair of pants','pair of shorts','set of shoes','set of sandals','blouse','set of socks','pair of underwear','jacket','coat','winter coat','sweatshirt','pair of jeans','cardigan']
                item = ['watch','scarf','bracelet','hat','beanie','head band','pair of glasses','set of earings','necklace']
                status = ['scuffed','dirty','well worn','simply designed','pristine','vibrant']
                size = ['large','small','very oversized','well fitting']

                u = random.randint(0,len(clothing)-1)
                v = random.randint(0,len(occasion)-1)
                w = random.randint(0,len(color)-1)
                x = random.randint(0,len(size)-1)
                y = random.randint(0,len(item)-1)
                z = random.randint(0,len(status)-1)

                # .encode() translate message output to 'a byte-like object' which is "required"
                # if 0 receieved, user wants clothing
                if message == '0':
                    retMessage = f'They wore a {color[w]} and {size[x]} {item[y]} which was {status[z]}.'
                    retMessage = retMessage.encode(FORMAT)
                    conn.sendall(retMessage)
                    connectionSet = False

                # if 1 receieved, user wants clothing
                elif message == '1':
                    retMessage = f'They wore what seemed to be a {status[z]} {color[w]} {clothing[u]} which was {occasion[v]} for the occasion.'
                    retMessage = retMessage.encode(FORMAT)
                    conn.sendall(retMessage)
                    connectionSet = False
