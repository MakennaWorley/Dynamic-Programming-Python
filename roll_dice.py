def roll_dice(N,M):
    dice_sides_value = [[0] * M] * N
    dice_sides_value[0] = [1] * 6 + [0] * (M - 6)

    for i in range(1, N):
        for j in reversed(range(M)):
            dice_sides_value[i][j] = 0
            for k in range(1, 7):
                if j - k >= 0:
                    dice_sides_value[i][j] += dice_sides_value[i - 1][j - k]

    return dice_sides_value[-1][-1]


if __name__ == "__main__":
    print(roll_dice(2,7))
    print(roll_dice(3,9))
    print(roll_dice(8,24))
