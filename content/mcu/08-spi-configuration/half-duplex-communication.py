import matplotlib.pyplot as plt
from matplotlib import patches

# 1. Canvas & Coordinate System Setup
fig, ax = plt.subplots(figsize=(10, 4.8), dpi=120)
ax.set_xlim(0, 92)
ax.set_ylim(14, 55)
ax.axis("off")

# 2. Master / Slave Outer Brackets & Titles
# Master Bracket (Left)
ax.plot([30, 30], [18, 50], color="black", lw=2.5)
ax.plot([30, 25], [50, 50], color="black", lw=2.5)
ax.plot([30, 25], [18, 18], color="black", lw=2.5)
ax.text(12.4, 51, "Master", fontsize=12, ha="center", fontweight="bold")

# Slave Bracket (Right)
ax.plot([60, 60], [18, 50], color="black", lw=2.5)
ax.plot([60, 65], [50, 50], color="black", lw=2.5)
ax.plot([60, 65], [18, 18], color="black", lw=2.5)
ax.text(78.3, 51, "Slave", fontsize=12, ha="center", fontweight="bold")

# 3. Functional Blocks (Shift Registers, Resister & Clock Generator)
# Master Shift Register
rect_m = patches.Rectangle((2, 40), 20, 6, facecolor="white", edgecolor="black")
ax.add_patch(rect_m)
ax.text(12, 43, "8-bit\nshift register", fontsize=9.5, ha="center", va="center")

# Slave Shift Register
rect_s = patches.Rectangle((68, 40), 20, 6, facecolor="white", edgecolor="black")
ax.add_patch(rect_s)
ax.text(78, 43, "8-bit\nshift register", fontsize=9.5, ha="center", va="center")

# Central Resister (R) Block
rect_r = patches.Rectangle(
    (44, 38), 2, 4, facecolor="purple", edgecolor="none", zorder=3
)
ax.add_patch(rect_r)
ax.text(45, 40, "R", fontsize=9.5, ha="center", va="center", color="white", zorder=4)

# SPI Clock Generator
rect_clk = patches.Rectangle((2, 28), 12, 6, facecolor="white", edgecolor="black")
ax.add_patch(rect_clk)
ax.text(8, 31, "SPI Clock\ngenerator", fontsize=9, ha="center", va="center")

# 4. Bit Order Annotations (MSBit <--- LSBit)
# Master Bit Order
ax.annotate(
    "",
    xy=(6, 47.5),
    xytext=(18, 47.5),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)
ax.text(4, 47, "MSBit", fontsize=8.5, ha="right")
ax.text(20, 47, "LSBit", fontsize=8.5, ha="left")

# Slave Bit Order
ax.annotate(
    "",
    xy=(72, 47.5),
    xytext=(84, 47.5),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)
ax.text(70, 47, "MSBit", fontsize=8.5, ha="right")
ax.text(86, 47, "LSBit", fontsize=8.5, ha="left")

# 5. Signal Bus Lines & Routing
# Line 1: MISO Line Routing & Master Entry
ax.plot([68, 45], [43, 43], color="black", lw=1.2)
ax.plot([26, 26], [43, 37], color="black", lw=1.2)
ax.annotate(
    "",
    xy=(22, 43),
    xytext=(26.2, 43),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)

# Line 1-1: Master Output -> MOSI Loop
ax.plot([0.1, 2], [43, 43], color="black", lw=1.2)
ax.plot([0.1, 0.1], [43, 37], color="black", lw=1.2)
ax.plot([0.1, 30], [37, 37], color="black", lw=1.2)

# Line 2: MOSI Line Routing & Slave Entry Loop
ax.plot([45, 45], [43, 37], color="black", lw=1.2)
ax.plot([30, 45], [37, 37], color="black", lw=1.2)
ax.plot([65, 90], [37, 37], color="black", lw=1.2)
ax.plot([65, 65], [37, 43], color="black", lw=1.2)
ax.plot([90.1, 90.1], [37, 43], color="black", lw=1.2)
ax.annotate(
    "",
    xy=(88, 43),
    xytext=(90.3, 43),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)

# Line 3: SCK (Serial Clock) Lines & Inputs
ax.plot([21, 60], [31, 31], color="black", lw=1.2)
ax.plot([14, 78], [31, 31], color="black", lw=1.2)
ax.annotate(
    "",
    xy=(18, 40),
    xytext=(18, 30.8),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)
ax.annotate(
    "",
    xy=(78, 40),
    xytext=(78, 30.8),
    arrowprops={"arrowstyle": "->", "lw": 1.2, "color": "black"},
)

# Line 4: NSS (Slave Select) Line & Square Marker
ax.plot([30, 60], [25, 25], color="black", lw=1.2)
ax.scatter([55], [25], marker="s", s=40, color="black", edgecolor="black")

# 6. Junction Dots & Text Annotations
# Junction Points (Dots)
for y_pos in [43, 37, 31, 25]:
    ax.scatter([30], [y_pos], color="black", s=50)
    ax.scatter([60], [y_pos], color="black", s=50)

# Bus Text Labels
ax.text(32, 44, "MISO", fontsize=9.5)
ax.text(56, 44, "MISO", fontsize=9.5)
ax.text(32, 38, "MOSI", fontsize=9.5)
ax.text(56, 38, "MOSI", fontsize=9.5)
ax.text(32, 32, "SCK", fontsize=9.5)
ax.text(56, 32, "SCK", fontsize=9.5)
ax.text(32, 26, "NSS", fontsize=9.5)
ax.text(56, 26, "NSS", fontsize=9.5)

# Directional Arrows on Bus Lines
ax.annotate(
    "",
    xy=(42, 44.5),
    xytext=(49, 44.5),
    arrowprops={"arrowstyle": "<->", "lw": 1.2, "color": "black"},
)
ax.annotate(
    "",
    xy=(42, 32.5),
    xytext=(49, 32.5),
    arrowprops={"arrowstyle": "<-", "lw": 1.2, "color": "black"},
)

# 7. Render & Export Image
plt.tight_layout()
plt.savefig("half-duplex-communication.svg", format="svg", dpi=300)
