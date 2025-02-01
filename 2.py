def most_expensive(x, last):
    ans = 1
    while x > 1:
        x //= 2
        ans *= 2
    if ans == last:
        ans = ans // 2
    return ans


def get_result(x):
    if x < 7:
        return -1
    first = most_expensive(x-3, 0)
    second = most_expensive(x - first - 1, first)
    third = most_expensive(x - first - second, second)
    return first + second + third


t = int(input())
answers = []

for _ in range(t):
    x = int(input())
    answers.append(get_result(x))

for answer in answers:
    print(answer)
