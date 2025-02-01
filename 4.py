def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return (a // greatest_common_divisor(a, b)) * b


def get_remainder_to_multiple(number, divisor):
    return (divisor - (number % divisor)) % divisor


def find_minimum_adjustment_cost():
    n, x, y, z = map(int, input().split())
    numbers = list(map(int, input().split()))

    xy = least_common_multiple(x, y)
    xz = least_common_multiple(x, z)
    yz = least_common_multiple(y, z)
    xyz = least_common_multiple(xy, z)
    INF = 10**18 + 1
    min_cost = [INF] * 8

    for value in numbers:
        cost_x = get_remainder_to_multiple(value, x)
        cost_y = get_remainder_to_multiple(value, y)
        cost_z = get_remainder_to_multiple(value, z)
        cost_xy = get_remainder_to_multiple(value, xy)
        cost_xz = get_remainder_to_multiple(value, xz)
        cost_yz = get_remainder_to_multiple(value, yz)
        cost_xyz = get_remainder_to_multiple(value, xyz)

        min_cost[1] = min(min_cost[1], cost_x)
        min_cost[2] = min(min_cost[2], cost_y)
        min_cost[4] = min(min_cost[4], cost_z)
        min_cost[3] = min(min_cost[3], cost_xy)
        min_cost[5] = min(min_cost[5], cost_xz)
        min_cost[6] = min(min_cost[6], cost_yz)
        min_cost[7] = min(min_cost[7], cost_xyz)

    result = min_cost[7]
    subsets = [1, 2, 4, 3, 5, 6, 7]

    for subset1 in subsets:
        for subset2 in subsets:
            if (subset1 | subset2) == 7:
                result = min(result, min_cost[subset1] + min_cost[subset2])

    for subset1 in subsets:
        for subset2 in subsets:
            for subset3 in subsets:
                if (subset1 | subset2 | subset3) == 7:
                    total_cost = min_cost[subset1] + min_cost[subset2] + min_cost[subset3]
                    result = min(result, total_cost)

    print(result)


find_minimum_adjustment_cost()
