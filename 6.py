def count_points_on_line(n, points):
    max_points_on_line = 0

    for i in range(n):
        for j in range(i + 1, n):
            count_on_line = 0
            x1, y1 = points[i]
            x2, y2 = points[j]

            for k in range(n):
                x, y = points[k]
                if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
                    count_on_line += 1

            max_points_on_line = max(max_points_on_line, count_on_line)

    return max_points_on_line


def get_result():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    max_in_line = count_points_on_line(n, points)

    if max_in_line <= (2 * n) // 3:
        print(n // 3)
    else:
        print(n - max_in_line)


get_result()
