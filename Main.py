import numpy as np
import matplotlib.pyplot as plt

steps = 10000
f = np.empty(steps)
t = np.empty(steps)
dt = 0.01

for i in range(steps):
    f[i] = np.sin(2 * np.pi * dt * i) + 0.5*np.sin(2 * np.pi * dt * i * 8) + 0.25*np.sin(2 * np.pi * dt * i * 5) + 1 + 0.2*np.sin(2 * np.pi* dt * i * 3)
    t[i] = dt*i
    t[i] = dt*i

real = np.fft.rfft(f, norm = 'forward')
complex = np.fft.fft(f, norm = 'forward')
real_freq = np.fft.rfftfreq(n = steps, d = dt)
freq = np.fft.fftfreq(n = len(complex), d = dt)

figure, axis = plt.subplots(3, 1, figsize=(15, 30))

axis[0].plot(real_freq, np.abs(real)) 
axis[0].set_title("Real Fourier Transform")
axis[0].set_xlabel("Frequency")
axis[0].set_ylabel("Amplitude")
axis[0].set_xlim([-10, 10])

axis[1].plot(freq, np.abs(complex)) 
axis[1].set_title("Complex Fourier Transform")
axis[1].set_xlabel("Frequency")
axis[1].set_ylabel("Amplitude")
axis[1].set_xlim([-10, 10])

axis[2].plot(t, f) 
axis[2].set_title("Original Wave")
axis[2].set_xlabel("Time")
axis[2].set_ylabel("Voltage")
axis[2].set_xlim([0, 10])

plt.tight_layout()
plt.show()