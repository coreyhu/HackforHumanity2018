import numpy as np
import matplotlib.pyplot as plt
import serial
from drawnow import drawnow
import time
import threading

plt.ion()
port = '/dev/cu.usbmodem14311'
baud = 9600
ser = serial.Serial(port, baud, timeout=0, bytesize=serial.FIVEBITS)

df  = open('data.csv', 'a')
y = []

def makeFig():
    plt.ylim(0,100)
    plt.ylabel('sensor output')
    plt.ticklabel_format(useOffset=False)
    plt.plot(y)


def log_data():
    delta_seconds = 0
    while True:
        val = ser.readline().decode()
        delta_seconds += 1
        y.append(val)
        df.write('{},{}\n'.format(delta_seconds, val))
        drawnow(makeFig)
        if(delta_seconds>50):
            y.pop(0)

    df.close()

if __name__ == "__main__":
    log_data()
