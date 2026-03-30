import numpy as np
import matplotlib.pyplot as plt

# Parametere
T = 1
t = np.linspace(0, T, 2000)

# Inngangssignal: 20 V p-p => amplitude 10 V
V1 = 10 * np.sin(2 * np.pi * t / T)

# Finn tidspunktene der signalet krysser nivåene
t1 = T/(2*np.pi) * np.arcsin(5.4/10)
t2 = T/2 - t1
t3 = T/2 + T/(2*np.pi) * np.arcsin(7.5/10)
t4 = T - T/(2*np.pi) * np.arcsin(7.5/10)

# Lag Vut
Vut = np.zeros_like(V1)

for i in range(len(t)):
    if 0 <= t[i] < t1:
        Vut[i] = -V1[i]
    elif t1 <= t[i] < t2:
        Vut[i] = -5.4
    elif t2 <= t[i] < t3:
        Vut[i] = -V1[i]
    elif t3 <= t[i] < t4:
        Vut[i] = 7.5
    else:
        Vut[i] = -V1[i]

# Plot
plt.figure(figsize=(10, 5))
plt.plot(t, V1, label='V1 (inngangsignal)')
plt.plot(t, Vut, color='red', linestyle='--', label='Vut')

# Marker viktige nivåer og fjern -5.0
yticks = list(plt.yticks()[0])
yticks.extend([-5.4, 7.5])
yticks = [y for y in yticks if abs(y + 5.0) > 1e-6]  # fjerner -5.0
yticks = sorted(set(np.round(yticks, 2)))
plt.yticks(yticks)

plt.xlabel('t [s]')
plt.ylabel('Spenning V [V]')
plt.title('Klippekrets med zenerdioder')
plt.grid()
plt.legend()
plt.show()