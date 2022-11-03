import os
import threading
import math

def startReceiver(fileName):
    os.system(f"python3 receiver.py {fileName}")

numberOfReceivers = int(input("Enter number of receivers:"))
receivers = []

for i in range(numberOfReceivers):
    startReceiverThread = threading.Thread(target = startReceiver,args = (f"receivedDataFiles/file{i+1}.txt",))
    receivers.append(startReceiverThread)
    startReceiverThread.start()

for i in range(numberOfReceivers):
    receivers[i].join()

print("Receiving finished...")
print("Connection closed...")
