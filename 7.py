MOD = 998244353


def add(x, y):
    return (x + y) % MOD


def mult(x, y):
    return (x * y) % MOD


def sub(x, y):
    return (x - y + MOD) % MOD


def get_result():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    prefix_sum = [0] * (k + 1)
    prefix_sum[0] = n

    for i in range(n):
        res = 1
        for j in range(1, k + 1):
            res = mult(res, a[i])
            prefix_sum[j] = add(prefix_sum[j], res)

    two_pow = [1] * (k + 1)
    for i in range(1, k + 1):
        two_pow[i] = mult(two_pow[i - 1], 2)

    C = [[0] * (k + 1) for _ in range(k + 1)]
    for i in range(k + 1):
        C[i][0] = C[i][i] = 1
        for j in range(1, i):
            C[i][j] = add(C[i - 1][j - 1], C[i - 1][j])

    inv_2 = 499122177

    for i in range(1, k + 1):
        A = 0
        for j in range(i + 1):
            res = mult(C[i][j], prefix_sum[j])
            res = mult(res, prefix_sum[i - j])
            A = add(A, res)
        B = mult(two_pow[i - 1], prefix_sum[i])
        A = mult(A, inv_2)
        print(sub(A, B))


get_result()
