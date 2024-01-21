import os
import socket
import threading
from datetime import datetime
#from track import detect 

'''
try:
    detect()
except:
    print("Detection terminated")
    
'''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
path = "/home/higopika/Desktop/client_program/waste-product-classification-client/detections/"

def get_version():
    return "1"

def send_data():
    VERSION = get_version()
    global client, path, host
    client.connect((host,5000))

    for i in os.listdir(path):
        i = path+i
        f = open(i, "r")
        data = f.read()
#        data = "1:" + data
        client.sendall(data.encode())
        f.close()
        os.remove(i)
    data = "DONE:" + VERSION
        

    
def recieve_data():
    done = False
    data = ""
    data = client.recv(7)
    if data[0:7] == b'<RIGHT>':
        return
    elif data[0:7] != b'<WRONG>':
        print(data[0:7])
        print("ERROR: Expected version RIGHT or WRONG")
        return
    else:
        done = False
        data = ""
        while not done:
            # Receive the data one byte at a time
            data = client.recv(1024)
            if(data[-5:] == b'<END>'):
                #if not data:
                done = True
                print("END")
 #               client.close()
                break
            else:
                file = open("best4.pt", "ab") # change 'w' to 'a'
                file.write(data)
                print("writing")
                file.close()
            #sys.stdout.write(data)



while True:

    if os.listdir(path) != []:
        send_data()
        recieve_data()
        client.close()

