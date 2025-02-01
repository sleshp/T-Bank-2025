def get_result():
    n, s = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        s = max(s, a[i])
        prefix_sum[i] = prefix_sum[i - 1] + a[i]

    j = 1
    cnt_close = [0] * (n + 1)

    for i in range(1, n + 1):
        while j <= n and prefix_sum[j] - prefix_sum[i - 1] <= s:
            j += 1
        if j == n + 1:
            break
        j -= 1
        cnt_close[j] += 1 + cnt_close[i - 1]

    ans = 0
    for i in range(1, n + 1):
        ans += cnt_close[i] * (n - i)

    ans += (n * (n + 1)) // 2
    print(ans)


get_result()
