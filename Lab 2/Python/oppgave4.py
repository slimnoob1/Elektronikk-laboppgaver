import numpy as np
import matplotlib.pyplot as plt

# V1-verdier
V1 = np.linspace(0, 10, 1000)

# Gitte verdier
I_max = 11.67  # mA
V_threshold = 3.62  # V

# Lineær sammenheng før terskel
slope = I_max / V_threshold

# Definer I_R3
I_R3 = np.where(V1 <= V_threshold, slope * V1, I_max)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(V1, I_R3, label=r'$I_{R3}(V_1)$')

# Marker terskelpunkt
plt.plot(V_threshold, I_max, 'ro')

# X-akse: 1V mellomrom + 3.62
xticks = list(np.arange(0, 11, 1))
xticks.append(V_threshold)
xticks.remove(4)
plt.xticks(sorted(set(xticks)))

# Y-akse: lag egne ticks uten 12 mA
yticks = list(np.arange(0, 11, 2))  # 0,2,4,...,10
yticks.append(I_max)                # legg til 11.67
plt.yticks(sorted(yticks))

# Labels
plt.xlabel('V1 (V)')
plt.ylabel('I_R3 (mA)')
plt.title(r'Kurve for $I_{R3}(V_1)$')
plt.grid(True)
plt.legend()

plt.xlim(0, 10)
plt.ylim(0, 13)

plt.show()