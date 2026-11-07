import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.patches import FancyArrowPatch

# 1. Figure 및 Axes 설정
fig, ax = plt.subplots(figsize=(13, 6))
ax.set_xlim(0, 14)
ax.set_ylim(0, 8)
ax.axis("off")

# 색상 정의
arrow_color = "black"

# 2. Master 및 Slave 박스 그리기
master_box = patches.Rectangle(
    (0.5, 2.0), 5.5, 3.5, facecolor="white", edgecolor="black", linewidth=1.5
)
slave_box = patches.Rectangle(
    (8.0, 2.0), 5.5, 3.5, facecolor="white", edgecolor="black", linewidth=1.5
)
ax.add_patch(master_box)
ax.add_patch(slave_box)

# 박스 내부 레이블
ax.text(0.8, 5.0, "Master", fontsize=13, fontweight="bold")
ax.text(8.3, 5.0, "Slave", fontsize=13, fontweight="bold")

ax.text(3.25, 4.8, "Shift Register", fontsize=12, ha="center")
ax.text(10.75, 4.8, "Shift Register", fontsize=12, ha="center")

# 3. Master 내부 시프트 레지스터: 1클럭 후 (B0가 추가되고 A7~A1 이동)
master_data = [
    ("B7", "gray", "white"),
    ("B6", "gray", "white"),
    ("B5", "gray", "white"),
    ("B4", "gray", "white"),
    ("B3", "gray", "white"),
    ("B2", "gray", "white"),
    ("B1", "gray", "white"),
    ("B0", "gray", "white"),
]
for i, (val, bg_color, txt_color) in enumerate(master_data):
    rect = patches.Rectangle(
        (1.0 + i * 0.55, 4.2), 0.55, 0.45, facecolor=bg_color, edgecolor="black"
    )
    ax.add_patch(rect)
    ax.text(
        1.275 + i * 0.55,
        4.425,
        val,
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=txt_color,
    )

# SPI clock generator 박스 (Master 내부)
clock_gen = patches.Rectangle(
    (2.3, 2.7), 2.0, 0.7, facecolor="white", edgecolor="black"
)
ax.add_patch(clock_gen)
ax.text(3.3, 3.05, "SPI clock\ngenerator", ha="center", va="center", fontsize=8.5)


# 4. Slave 내부 시프트 레지스터: 1클럭 후 (A0가 추가되고 B7~B1 이동)
slave_data = [
    ("A7", "white", "black"),
    ("A6", "white", "black"),
    ("A5", "white", "black"),
    ("A4", "white", "black"),
    ("A3", "white", "black"),
    ("A2", "white", "black"),
    ("A1", "white", "black"),
    ("A0", "white", "black"),
]
for i, (val, bg_color, txt_color) in enumerate(slave_data):
    rect = patches.Rectangle(
        (8.6 + i * 0.55, 4.2), 0.55, 0.45, facecolor=bg_color, edgecolor="black"
    )
    ax.add_patch(rect)
    ax.text(
        8.875 + i * 0.55,
        4.425,
        val,
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=txt_color,
    )

# 5. 주황색 신호선 (주요 경로 연결)

# (A) SPI Clock Generator -> Master Shift Register 수직 화살표 추가 (A4 위치로 들어감)
ax.plot([3.3, 3.3], [3.4, 4.2], color=arrow_color, lw=2)
arrow_clk_master = FancyArrowPatch(
    (3.3, 3.9),
    (3.3, 4.2),
    arrowstyle="->,head_width=4,head_length=6",
    color=arrow_color,
    lw=2,
)
ax.add_patch(arrow_clk_master)

# (B) MOSI 라인: Master A0(5.4) -> Master 경계(6.0) -> Slave 경계(8.0) -> Slave B7(8.6)
ax.plot([5.4, 6.0], [4.425, 4.425], color=arrow_color, lw=2)
ax.plot([6.0, 8.0], [4.425, 4.425], color=arrow_color, lw=2)
arrow_mosi_in = FancyArrowPatch(
    (8.0, 4.425),
    (8.6, 4.425),
    arrowstyle="->,head_width=4,head_length=6",
    color=arrow_color,
    lw=2,
)
ax.add_patch(arrow_mosi_in)

# (C) SCLK 라인: Clock Gen(4.3) -> Master 경계(6.0) -> Slave 경계(8.0) -> B4 내부 연결(10.55)
ax.plot([4.3, 6.0], [3.05, 3.05], color=arrow_color, lw=2)
ax.plot([6.0, 8.0], [3.05, 3.05], color=arrow_color, lw=2)
ax.plot([8.0, 10.55, 10.55], [3.05, 3.05, 4.2], color=arrow_color, lw=2)
arrow_sclk_in = FancyArrowPatch(
    (10.55, 3.9),
    (10.55, 4.2),
    arrowstyle="->,head_width=4,head_length=6",
    color=arrow_color,
    lw=2,
)
ax.add_patch(arrow_sclk_in)

# (D) MISO 환형 루프 라인: Slave B0 끝(13.0) -> Slave 우측 경계 밖 -> 하단 -> Master 좌측 밖 -> Master A7(1.0)
ax.plot(
    [13.0, 13.75, 13.75, 0.25, 0.25, 1.0],
    [4.425, 4.425, 1.3, 1.3, 4.425, 4.425],
    color=arrow_color,
    lw=2,
)
arrow_miso_in = FancyArrowPatch(
    (0.7, 4.425),
    (1.0, 4.425),
    arrowstyle="->,head_width=4,head_length=6",
    color=arrow_color,
    lw=2,
)
ax.add_patch(arrow_miso_in)

# 경계 점(접점) 포인트 표시
dots_x = [6.0, 6.0, 8.0, 8.0, 13.75, 0.25]
dots_y = [4.425, 3.05, 4.425, 3.05, 4.425, 4.425]
ax.scatter(dots_x, dots_y, color="black", s=20, zorder=5)

# 6. 중앙 통신선 라벨 및 흐름 방향 화살표
# MOSI (상단)
ax.text(7.0, 4.5, "MOSI", fontsize=11, ha="center")

# SCLK (중단)
ax.text(7.0, 3.1, "SCLK", fontsize=11, ha="center")

# MISO (하단)
ax.text(7.0, 1.4, "MISO", fontsize=11, ha="center")

# 7. 상단 SCLK 클럭 파형
ax.text(0.8, 6.3, "SCLK", fontsize=11, fontweight="bold")
clock_x = [
    2.0,
    2.5,
    2.5,
    3.0,
    3.0,
    3.5,
    3.5,
    4.0,
    4.0,
    4.5,
    4.5,
    5.0,
    5.0,
    5.5,
    5.5,
    6.0,
    6.0,
    6.5,
    6.5,
    7.0,
    7.0,
    7.5,
    7.5,
    8.0,
    8.0,
    8.5,
    8.5,
    9.0,
    9.0,
    9.5,
    9.5,
    10.0,
    10.0,
    10.5,
]
clock_y = [
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
    6.0,
    6.0,
    6.5,
    6.5,
]
ax.plot(clock_x, clock_y, color="black", linestyle="--", linewidth=2)
ax.plot(clock_x[0:33], clock_y[0:33], color="red", linewidth=2.5)

plt.tight_layout()

plt.savefig("spi-behind-the-scene-8.png", format="png", bbox_inches="tight")
