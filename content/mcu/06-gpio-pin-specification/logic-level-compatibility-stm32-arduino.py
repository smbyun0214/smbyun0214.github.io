import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(11, 7))

# 전체 제목 및 축 설정 (5V 출력을 수용할 수 있도록 ylim 확장)
ax.set_xlim(0, 2.2)
ax.set_ylim(-0.8, 5.6)

# ==========================================
# 1. Noise Margin 영역 추가 (출력과 입력 사이)
# ==========================================
# 상단 Noise Margin (2.9V ~ 3.0V 사이)
ax.add_patch(
    patches.Rectangle((0.8, 2.9), 0.6, 0.1, facecolor="#d9d9d9", edgecolor="none")
)
ax.text(1.1, 2.95, "Noise margin", ha="center", va="center", fontsize=10)

# 하단 Noise Margin (0.4V ~ 1.5V 사이)
ax.add_patch(
    patches.Rectangle((0.8, 0.4), 0.6, 1.1, facecolor="#d9d9d9", edgecolor="none")
)
ax.text(1.1, 0.95, "Noise Margin", ha="center", va="center", fontsize=10)

# ==========================================
# 2. 왼쪽: STM32 Digital pin output (X: 0.2 ~ 0.8)
# ==========================================
ax.text(
    0.5, 3.4, "(STM32 Digital pin output)", ha="center", fontsize=10, fontweight="bold"
)

# Logic level 0 (0 ~ 0.4V)
ax.add_patch(patches.Rectangle((0.2, 0), 0.6, 0.4, facecolor="blue", edgecolor="black"))
ax.text(0.5, 0.2, "Logic level 0", color="white", ha="center", va="center", fontsize=10)

# Intermediate region (0.4 ~ 2.9V)
ax.add_patch(
    patches.Rectangle((0.2, 0.4), 0.6, 2.5, facecolor="gray", edgecolor="black")
)
ax.text(0.5, 1.65, "Intermediate region", ha="center", va="center", fontsize=10)

# Logic level 1 (2.9 ~ 3.3V)
ax.add_patch(
    patches.Rectangle((0.2, 2.9), 0.6, 0.4, facecolor="orange", edgecolor="black")
)
ax.text(0.5, 3.1, "Logic level 1", ha="center", va="center", fontsize=10)

# Label (Left)
ax.text(
    0.18, 0.4, r"$\text{V}_\text{OL(Max)}$ (0.4V)", va="center", ha="right", fontsize=10
)
ax.text(
    0.18, 2.9, r"$\text{V}_\text{OH(Min)}$ (2.9V)", va="center", ha="right", fontsize=10
)
ax.text(0.18, 3.3, r"$\text{V}_\text{DD}$ (3.3V)", va="center", ha="right", fontsize=10)

# ==========================================
# 3. 오른쪽: Arduino Digital pin input (X: 1.4 ~ 2.0)
# ==========================================
ax.text(
    1.7, 5.1, "(Arduino Digital pin input)", ha="center", fontsize=10, fontweight="bold"
)

# Logic level 0 (0 ~ 1.5V)
ax.add_patch(patches.Rectangle((1.4, 0), 0.6, 1.5, facecolor="blue", edgecolor="black"))
ax.text(
    1.7, 0.75, "Logic level 0", color="white", ha="center", va="center", fontsize=10
)

# Intermediate region (1.5 ~ 3.0V)
ax.add_patch(
    patches.Rectangle((1.4, 1.5), 0.6, 1.5, facecolor="gray", edgecolor="black")
)
ax.text(1.7, 2.25, "Intermediate region", ha="center", va="center", fontsize=10)

# Logic level 1 (3.0 ~ 5.0V)
ax.add_patch(
    patches.Rectangle((1.4, 3.0), 0.6, 2.0, facecolor="orange", edgecolor="black")
)
ax.text(1.7, 4.0, "Logic level 1", ha="center", va="center", fontsize=10)

# Label (Right)
ax.text(
    2.02, 1.5, r"$\text{V}_\text{IL(Max)}$ (1.5V)", va="center", ha="left", fontsize=10
)
ax.text(
    2.02, 3.0, r"$\text{V}_\text{IH(Min)}$ (3V)", va="center", ha="left", fontsize=10
)
ax.text(2.02, 5.0, r"$\text{V}_\text{CC}$ (5V)", va="center", ha="left", fontsize=10)

# ==========================================
# 4. 전압 경계선 및 레이블 표시
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
    "logic-level-compatibility-stm32-arduino.svg", format="svg", bbox_inches="tight"
)
