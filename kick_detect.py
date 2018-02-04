import numpy as np
import matplotlib.pyplot as plt
import serial
from drawnow import drawnow
import numpy as np
import pandas as pd
from scipy.signal import find_peaks_cwt
import time
import struct

plt.ion()
port = '/dev/cu.usbmodem1451'
baud = 9600
ser = serial.Serial(port, baud, timeout=0)

df = open('data.csv', 'a')
y = []

def makeFig():
    # start = time.time()
    # print('makefig start:', start)
    plt.ylim(0,2000)
    plt.ylabel('sensor output')
    plt.ticklabel_format(useOffset=False)
    plt.plot(y)
    # print('makefig end:', time.time())
    # print(time.time() - start)

def log_data():

    delta_seconds = 0
    while True:
        start = time.time()
        print('log data start:', start)
        sig = ser.readline()
        if b'\r' in sig:
            val = int(sig[:sig.index(b'\r')].decode('utf-8'))
            delta_seconds += 1
            y.append(val)
            print("val:", val)
            df.write('{},{}\n'.format(delta_seconds, val))
            drawnow(makeFig)
            if delta_seconds > 50:
                y.pop(0)
        print('log data end:', time.time())
        print(time.time() - start)


    df.close()

def find_peaks():
    df = pd.read_csv('data.csv', names=['time', 'signal'])
    indexes = find_peaks_cwt(df['signal'], np.arange(1, df.shape[0]))
    return indexes


if __name__ == "__main__":
    # log_data()
    find_peaks()
