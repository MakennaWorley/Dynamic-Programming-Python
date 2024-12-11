def climb_stair(n):
    stairs = [1] * (n + 1)

    for i in range(2, n + 1):
        stairs[i] = stairs[i - 1] + stairs[i - 2]
    return stairs[-1]


if __name__ == "__main__":
    print(climb_stair(10))
    print(climb_stair(20))
    print(climb_stair(30))

