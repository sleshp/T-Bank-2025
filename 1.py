def get_result():
    s = input()
    pos_r = 0
    pos_m = 0
    for i in range(3):
        if s[i] == 'R':
            pos_r = i
        if s[i] == 'M':
            pos_m = i
    if pos_r < pos_m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    get_result()
