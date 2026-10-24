import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

# 1. Very High Speed
t_vhigh = [0, 1, 1.2, 8.8, 9, 10, 10.2, 17.8, 18, 19]
v_vhigh = [0, 0, 3.3, 3.3, 0, 0, 3.3, 3.3, 0, 0]

# 2. High Speed
t_high = [0, 1, 1.8, 8.2, 9, 10, 10.8, 17.2, 18, 19]
v_high = [0, 0, 3.3, 3.3, 0, 0, 3.3, 3.3, 0, 0]

# 3. Medium Speed
t_med = [0, 1, 2.5, 7.5, 9, 10, 11.5, 16.5, 18, 19]
v_med = [0, 0, 3.3, 3.3, 0, 0, 3.3, 3.3, 0, 0]

# 4. Low Speed
t_low = [0, 1, 3, 7, 9, 10, 12, 16, 18, 19]
v_low = [0, 0, 3.3, 3.3, 0, 0, 3.3, 3.3, 0, 0]

plt.plot(t_vhigh, v_vhigh, label="1. Very High")
plt.plot(t_high, v_high, label="2. High")
plt.plot(t_med, v_med, label="3. Medium")
plt.plot(t_low, v_low, label="4. Low")

plt.title("GPIO Slew Rate Comparison by Speed Levels")
plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.ylim(-0.5, 4.0)
plt.xlim(0.0, 19.0)
plt.axhline(0, color="gray", linestyle="--")
plt.axhline(3.3, color="gray", linestyle="--")
plt.legend(loc="upper right")
plt.grid(True, linestyle=":", alpha=0.7)

plt.tight_layout()
plt.savefig("gpio-slew-rate-slopes-compared.svg", dpi=300)
plt.show()
