아래는 코드 설명을 더욱 상세하게 작성한 GitHub README 예시입니다.

---

# Moving Clock

## 개요

이 프로젝트는 Python의 `matplotlib` 라이브러리와 `numpy`를 사용하여 실시간으로 움직이는 아날로그 시계를 구현한 것입니다. 이 시계는 시침, 분침, 초침이 실제 시계처럼 12시부터 12시간까지 주기를 맞춰 움직이며, `FuncAnimation`을 사용해 애니메이션 효과를 제공합니다.

## 주요 기능

- **시침, 분침, 초침**: 각각 시간이 흐를 때마다 움직이며, 12시 40분에서 시작하여 시간이 경과하는 모습을 시각적으로 표현합니다.
- **애니메이션**: `FuncAnimation`을 사용하여 1초마다 시침, 분침, 초침이 갱신됩니다.
- **시계 원과 눈금**: 시계의 원과 눈금을 그려 실제 시계처럼 보이게 합니다.

## 코드 설명

이 코드는 3개의 주요 부분으로 나눠져 있습니다:

### 1. 시계 원과 눈금 그리기
```python
# 시계의 원 그리기
circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
ax.add_artist(circle)
```
- 시계의 원을 그려서 시계의 테두리를 만듭니다. `plt.Circle`을 사용하여 원의 중심 `(0, 0)`과 반지름 `1`을 지정하고, `color='black'`으로 테두리를 검은색으로 설정합니다.

```python
# 시계 눈금 그리기
for i in range(12):
    angle = np.deg2rad(-i * 30 + 60)  # 12시가 맨 위로 오도록 각도 보정
    ax.text(0.85 * np.cos(angle), 0.85 * np.sin(angle), str(i + 1),
            horizontalalignment='center', verticalalignment='center', fontsize=12)
```
- `for` 루프를 통해 시계의 1부터 12까지 숫자를 원주에 배치합니다. 각도 계산을 통해 숫자가 시계 원의 적절한 위치에 배치되도록 합니다.

### 2. 시침, 분침, 초침 초기화
```python
# 시침, 분침, 초침 초기화
hour_hand, = ax.plot([], [], linewidth=6, color='black', label='Hour Hand')
minute_hand, = ax.plot([], [], linewidth=4, color='blue', label='Minute Hand')
second_hand, = ax.plot([], [], linewidth=2, color='red', label='Second Hand')
```
- 시침(`hour_hand`), 분침(`minute_hand`), 초침(`second_hand`)을 `ax.plot()`을 사용하여 초기화합니다. 이들은 각각 선의 두께와 색상으로 구분됩니다.

### 3. 애니메이션 업데이트 함수
```python
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
```
- 이 함수는 `FuncAnimation`의 `frame`마다 호출되어 각 바늘의 각도를 업데이트합니다.
- 초침, 분침, 시침은 각기 다른 주기로 회전하며, `second_angle`, `minute_angle`, `hour_angle`의 값을 갱신합니다. 각 바늘의 끝점(`hour_x`, `hour_y`, `minute_x`, `minute_y`, `second_x`, `second_y`)은 삼각함수(`cos`, `sin`)를 사용해 계산됩니다.
- 시침은 12시간 주기로, 분침은 60분 주기로, 초침은 60초 주기로 회전합니다.

### 4. 애니메이션 생성
```python
# 애니메이션 생성
ani = FuncAnimation(fig, update, interval=1000)  # 1초마다 업데이트
```
- `FuncAnimation`을 사용해 1초 간격으로 `update` 함수가 호출되도록 설정합니다.

### 5. 시계 설정 및 시각화
```python
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
```
- `ax.set_xlim`과 `ax.set_ylim`으로 시계의 크기를 설정합니다.
- `ax.set_aspect('equal')`로 가로세로 비율을 동일하게 만들어 시계가 왜곡되지 않도록 합니다.
- x축과 y축의 눈금은 `ax.set_xticklabels([])`와 `ax.set_yticklabels([])`로 제거합니다.
- `plt.show()`를 호출하여 시계를 화면에 표시합니다.

## 필요 라이브러리

- `matplotlib`: 2D 그래프 및 애니메이션을 위한 라이브러리.
- `numpy`: 수학적 계산을 위한 라이브러리.

설치 방법:

```bash
pip install matplotlib numpy
```

## 사용 방법

1. 위 코드를 실행하여 동적인 시계 애니메이션을 확인합니다.
2. `FuncAnimation`의 `interval` 값을 변경하여 업데이트 주기를 조정할 수 있습니다.

## 예시 화면

![image](https://github.com/user-attachments/assets/54c7649b-d545-4901-96fd-7fb4754c9dfc)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

이 README 파일은 코드의 각 부분에 대한 자세한 설명을 포함하여 프로젝트를 이해하는 데 도움을 줍니다.
