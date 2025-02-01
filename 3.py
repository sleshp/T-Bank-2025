def get_result():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = a[0]
    y = a[1]

    a.sort()
    m += 2
    mn_raz_x = 1e18
    ans = 1e18

    for r in range(m - 1, n):
        l = r - m + 1
        mn_raz_x = min(abs(a[l] - x), mn_raz_x)
        mn_raz_y = abs(a[r] - y)
        ans = min(ans, mn_raz_x + mn_raz_y)

    print(int(ans))


get_result()
