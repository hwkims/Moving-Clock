import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 시계 그리기
fig, ax = plt.subplots(figsize=(6, 6))

# 시계의 원 그리기
circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
ax.add_artist(circle)

# 시계 눈금 그리기
for i in range(12):
    angle = np.deg2rad(-i * 30 + 60)  # 12시가 맨 위로 오도록 각도 보정
    ax.text(0.85 * np.cos(angle), 0.85 * np.sin(angle), str(i + 1),
            horizontalalignment='center', verticalalignment='center', fontsize=12)

# 시침, 분침, 초침 초기화
hour_hand, = ax.plot([], [], linewidth=6, color='black', label='Hour Hand')
minute_hand, = ax.plot([], [], linewidth=4, color='blue', label='Minute Hand')
second_hand, = ax.plot([], [], linewidth=2, color='red', label='Second Hand')

# 각도 초기화 (12시 40분)
hour_angle = 30  # 12시에서 30도 (1시간)
minute_angle = 240  # 40분에서 240도 (40분)
second_angle = 0  # 초침 초기화

# 애니메이션 업데이트 함수
def update(frame):
    global hour_angle, minute_angle, second_angle

    # 초침 업데이트
    second_angle -= 6  # 초침: 360도 / 60초 = 6도
    if second_angle >= 360:
        second_angle = 0
        minute_angle -= 6  # 분침: 360도 / 60분 = 6도
        if minute_angle >= 360:
            minute_angle = 0
            hour_angle -= 30  # 시침: 360도 / 12시간 = 30도
            if hour_angle >= 360:
                hour_angle = 0

    # 시침, 분침, 초침의 끝점 계산
    hour_x = 0.5 * np.cos(np.deg2rad(hour_angle + 90))  # +90도 보정으로 시계방향으로 이동
    hour_y = 0.5 * np.sin(np.deg2rad(hour_angle + 90))

    minute_x = 0.7 * np.cos(np.deg2rad(minute_angle + 90))  # +90도 보정
    minute_y = 0.7 * np.sin(np.deg2rad(minute_angle + 90))

    second_x = 0.9 * np.cos(np.deg2rad(second_angle + 90))  # +90도 보정
    second_y = 0.9 * np.sin(np.deg2rad(second_angle + 90))

    # 시침, 분침, 초침 업데이트
    hour_hand.set_data([0, hour_x], [0, hour_y])
    minute_hand.set_data([0, minute_x], [0, minute_y])
    second_hand.set_data([0, second_x], [0, second_y])

    return hour_hand, minute_hand, second_hand

# 애니메이션 생성
ani = FuncAnimation(fig, update, interval=1000)  # 1초마다 업데이트

# 시계 설정
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_xticklabels([])  # x축 눈금 제거
ax.set_yticklabels([])  # y축 눈금 제거

# 레이블 및 제목 설정
ax.set_title('Moving Clock', va='bottom')

# 그래프 표시
plt.legend()
plt.show()
