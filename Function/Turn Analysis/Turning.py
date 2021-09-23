import numpy as np


def check_turn(angle, start, end):
    x = angle.iloc[start] - angle.iloc[end]
    turn = 0
    if x < 0:
        if abs(x) > 180:
            turn = 'Left'
        else:
            turn = 'Right'
    if x > 0:
        if abs(x) > 180:
            turn = 'Right'
        else:
            turn = 'Left'
    return turn


def quality_turn(speed, start, end):
    x = np.array(speed.iloc[start:end+1])
    n = len(x)

    score = 0
    for i in range(n):
        if speed.iloc[start+i] >= speed.iloc[start + i + 1]:
            score += 1
        else:
            score += 0
    return round((score / (n)) * 100, 2)
