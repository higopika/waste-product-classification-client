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
path = "detections/"

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
    print("Should have recieved <WRONG> ",data)
    
    file_path = "best93_8_new.pt"
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")

    if data[0:7] == b'<RIGHT>':
        return
    elif data[0:7] != b'<WRONG>':
        print(data[0:7])
        print("ERROR: Expected version RIGHT or WRONG")
        return
    else:
        done = False
        data = ""
        file = open(file_path, "ab") # change 'w' to 'a'
        while not done:
            # Receive the data one byte at a time
            data = client.recv(1024)
            if(data[-5:] == b'<END>'):
                #if not data:
                done = True
                print("END")
                file.write(data[:-5])
 #               client.close()
                break
            else:                
                #print(data)
                file.write(data)
                print("writing")
        file.close()
            #sys.stdout.write(data)



while True:

    if os.listdir(path) != []:
        send_data()
        recieve_data()
        client.close()

