import time
import threading
from threading import Thread
import os#Members: Me, John, Solomon, Jac, Krystian
from colorama import init
init()
def incoming():#recieve msg
    file = open(r"mymessage.txt","r")
    incoming = file.read()
    time.sleep(0.1)
    print(incoming)
    file.close()
def outgoing():
    while 0==0:
        file = open(r"mymessage.txt", "a")
        file.write("\n")
        text = input(r"")
        if text == "WIPE":
            wipe()
        if "sudo" in text.lower():
            text = text[5:]
            file.write(text)
            file.close()
        else:
            file.write("Ethan: "+text)#CHANGE 'ETHAN' TO YOUR NAME!
            file.close()
        clear()
        incoming()

def wipe():
    file = open(r"mymessage.txt", "w")
    file.close
def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def helpa():
    print("To recieve a message press enter/send a message.\nType WIPE to clear the chat\n")    
#THREAD                                                   THREAD
thread_running = True
def my_forever_while():
    global thread_running
    #file = open(r"O:\Students\Curriculum\Computer Science\New folder (2)\New Text Document.txt", "r")

    start_time = time.time()
    #run this while there is no input
    while thread_running:
        incoming()


       
if __name__ == '__main__':
    t1 = Thread(target=my_forever_while)
    t2 = Thread(target=outgoing)
    t1.start()
    t2.start()
#THREAD                                                   THREAD
