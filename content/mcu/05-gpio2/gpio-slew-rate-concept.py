import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

time = [0, 1, 3, 7, 9, 10, 12, 16, 18, 19]
voltage = [0, 0, 3.3, 3.3, 0, 0, 3.3, 3.3, 0, 0]

plt.plot(time, voltage, label="GPIO Output")

plt.annotate(
    r"$\text{T}_\text{rise}$",
    xy=(2, 1.65),
    xytext=(0.8, 2.475),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
    fontsize=13,
)
plt.annotate(
    r"$\text{T}_\text{fall}$",
    xy=(8, 1.65),
    xytext=(8.8, 2.475),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
    fontsize=13,
)

plt.title(
    r"GPIO Slew Rate: $\text{T}_\text{rise}$ & $\text{T}_\text{fall}$ Timings Concept"
)
plt.xlabel("Time")
plt.ylabel("Voltage (V)")
plt.ylim(-0.5, 4.0)
plt.xlim(0.0, 19.0)
plt.axhline(0, color="gray", linestyle="--")
plt.axhline(3.3, color="gray", linestyle="--")
plt.legend(loc="upper right")
plt.grid(True, linestyle=":", alpha=0.7)

plt.tight_layout()
plt.savefig("gpio-slew-rate-concept.svg", dpi=300)
plt.show()
