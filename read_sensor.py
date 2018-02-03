import queue
import threading
import serial
import time


port = '/dev/cu.usbmodem1451'
baud = 9600

class mySerial(threading.Thread):
    def __init__(self, queue):
        super(mySerial, self).__init__()
        self.queue = queue #the received data is put in a queue
        self.buffer = ''
        self.ser = serial.Serial(port=port, baudrate=baud)

    def run(self):              
    while True:
        self.buffer += self.ser.read(self.ser.inWaiting()) #read all char in buffer
        while '\n' in self.buffer: #split data line by line and store it in var
            var, self.buffer = self.buffer.split('\n', 1)
            self.queue.put(var) #put received line in the queue
        time.sleep(0.01)   #do not monopolize CPU



class Base():
    def __init__(self):
        self.queue = queue.Queue(0) #create a new queue
        self.ser = mySerial(self.queue) 
        self.ser.start() #run thread


    def main(self   ):
        while(True):
            try:
                var = self.queue.get(False) #try to fetch a value from queue
            except queue.Empty: 
                pass #if it is empty, do nothing
            else:
                print(var) 


if __name__ == '__main__':
    b = Base() 
    b.main()