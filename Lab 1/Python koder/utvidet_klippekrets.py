import numpy as np
import matplotlib.pyplot as plt

# Parametere
T = 1
t = np.linspace(0, T, 1000)

# Inngangssignal (20 V p-p → amplitude 10 V)
V1 = 10 * np.sin(2 * np.pi * t / T)

# Utgangsspenning V0 (symmetrisk klipping)
V0 = np.zeros_like(V1)

for i in range(len(V1)):
    if V1[i] > 0.7:
        V0[i] = 0.7
    elif V1[i] < -0.7:
        V0[i] = -0.7
    else:
        V0[i] = V1[i]

# Plot
plt.figure()
plt.plot(t, V1, label='V1 (inngangsignal)')

# Del signalet ved T/2
mask1 = t <= T/2
mask2 = t > T/2

# V0: stiplet hele veien
plt.plot(t[mask1], V0[mask1], color='red', linestyle='--', label='V0 (over parallellen)')
plt.plot(t[mask2], V0[mask2], color='red', linestyle='--')

# Legg til ±0.7 som ticks og fjern 0
yticks = list(plt.yticks()[0])
yticks.extend([0.7, -0.7])
yticks = [y for y in yticks if abs(y) > 1e-9]  # fjerner 0
plt.yticks(sorted(yticks))

plt.xlabel('t [s]')
plt.ylabel('Spenningen V [V]')
plt.title('Utvidet klippekrets')
plt.legend()
plt.grid()

plt.show()