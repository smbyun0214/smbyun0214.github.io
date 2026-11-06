import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(11, 7))

# 전체 제목 및 축 설정 (5V 출력을 수용할 수 있도록 ylim 확장)
ax.set_xlim(0, 2.2)
ax.set_ylim(-0.8, 5.6)

# ==========================================
# 1. Noise Margin 영역 추가 (출력과 입력 사이)
# ==========================================
# 하단 Noise Margin (0.8V ~ 0.99V 사이)
ax.add_patch(
    patches.Rectangle((0.8, 0.8), 0.6, 0.19, facecolor="#d9d9d9", edgecolor="none")
)
ax.text(1.1, 0.895, "Noise Margin", ha="center", va="center", fontsize=10)

# ==========================================
# 2. 왼쪽: Arduino Digital pin output (X: 0.2 ~ 0.8)
# ==========================================
ax.text(
    0.5,
    5.1,
    "(Arduino Digital pin output)",
    ha="center",
    fontsize=10,
    fontweight="bold",
)

# Logic level 0 (0 ~ 0.8V)
ax.add_patch(patches.Rectangle((0.2, 0), 0.6, 0.8, facecolor="blue", edgecolor="black"))
ax.text(0.5, 0.4, "Logic level 0", color="white", ha="center", va="center", fontsize=10)

# Intermediate region (0.8 ~ 4.1V)
ax.add_patch(
    patches.Rectangle((0.2, 0.8), 0.6, 3.3, facecolor="gray", edgecolor="black")
)
ax.text(0.5, 2.45, "Intermediate region", ha="center", va="center", fontsize=10)

# Logic level 1 (4.1 ~ 5.0V)
ax.add_patch(
    patches.Rectangle((0.2, 4.1), 0.6, 0.9, facecolor="orange", edgecolor="black")
)
ax.text(0.5, 4.55, "Logic level 1", ha="center", va="center", fontsize=10)

# Label (Left)
ax.text(
    0.18, 0.8, r"$\text{V}_\text{OL(Max)}$ (0.8V)", va="center", ha="right", fontsize=10
)
ax.text(
    0.18, 4.1, r"$\text{V}_\text{OH(Min)}$ (4.1V)", va="center", ha="right", fontsize=10
)
ax.text(0.18, 5.0, r"$\text{V}_\text{CC}$ (5V)", va="center", ha="right", fontsize=10)

# ==========================================
# 3. 오른쪽: STM32 Digital pin input (X: 1.4 ~ 2.0)
# ==========================================
ax.text(
    1.7, 3.4, "(STM32 Digital pin input)", ha="center", fontsize=10, fontweight="bold"
)

# Logic level 0 (0 ~ 0.99V)
ax.add_patch(
    patches.Rectangle((1.4, 0), 0.6, 0.99, facecolor="blue", edgecolor="black")
)
ax.text(
    1.7, 0.495, "Logic level 0", color="white", ha="center", va="center", fontsize=10
)

# Intermediate region (0.99 ~ 2.31V)
ax.add_patch(
    patches.Rectangle((1.4, 0.99), 0.6, 1.32, facecolor="gray", edgecolor="black")
)
ax.text(1.7, 1.65, "Intermediate region", ha="center", va="center", fontsize=10)

# Logic level 1 (2.31 ~ 3.3V)
ax.add_patch(
    patches.Rectangle((1.4, 2.31), 0.6, 0.99, facecolor="orange", edgecolor="black")
)
ax.text(1.7, 2.805, "Logic level 1", ha="center", va="center", fontsize=10)

# Label (Right)
ax.text(
    2.02,
    0.99,
    r"$\text{V}_\text{IL(Max)}$ (0.99V)",
    va="center",
    ha="left",
    fontsize=10,
)
ax.text(
    2.02,
    2.31,
    r"$\text{V}_\text{IH(Min)}$ (2.31V)",
    va="center",
    ha="left",
    fontsize=10,
)
ax.text(2.02, 3.3, r"$\text{V}_\text{DD}$ (3.3V)", va="center", ha="left", fontsize=10)

# ==========================================
# 4. 하단 레이블 및 축 설정
# ==========================================
# X축 눈금 제거
ax.set_xticks([])
ax.set_yticks([])

# ==========================================
# 5. 플롯 테두리(Spines) 제거
# ==========================================
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()

plt.savefig(
    "logic-level-compatibility-arduino-stm32.svg", format="svg", bbox_inches="tight"
)
