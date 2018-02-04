
# coding: utf-8

# In[34]:


import pandas as pd
from scipy.signal import find_peaks_cwt
import matplotlib.pyplot as plt
from scipy.signal import lfilter

df = pd.read_csv('data.csv', names=['time', 'signal'])
df.head()
df = df.drop(df.index[[0, -1]])
df = df.dropna()

time = df['time']
signal = df['signal']
signal = signal.astype(float, casting='safe')

n = 15
b = [1.0 / n] * n
a = 1
l_signal = lfilter(b, a, signal)
l_indexes = find_peaks_cwt(l_signal, time, noise_perc=10)

l_peak_sigs = [l_signal[index] for index in l_indexes]
l_peak_time = [time[index] for index in l_indexes]

plt.plot(time, l_signal)
plt.plot(l_peak_time, l_peak_sigs, '*')

i = 0
limit = 3
threshold = 400
list_size = len(l_peak_time)

kick_first = False

if l_peak_sigs[i] < threshold:
    kick_first = True

while i < list_size - 1:

    if i < list_size - 1 and (l_peak_time[i] + limit > l_peak_time[i + 1] or l_peak_sigs[i + 1] < threshold):
        l_peak_time.pop(i + 1)
        l_peak_sigs.pop(i + 1)
        list_size -= 1
        i -= 1

    i += 1

if kick_first:
    l_peak_time.pop(0)
    l_peak_sigs.pop(0)

plt.plot(time, l_signal)
plt.plot(l_peak_time, l_peak_sigs, '*')

print("We believe your fetus has {} ± {} kicks".format(len(l_peak_time), 1))