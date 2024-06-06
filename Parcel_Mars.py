# номер посылки: 115014327
def min_platforms_needed(weights: list[int], limit: int) -> int:
    weights.sort()
    left, right = 0, len(weights) - 1
    platforms = 0

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
        right -= 1
        platforms += 1

    return platforms


if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    weights = list(map(int, data[:-1]))
    limit = int(data[-1])

    print(min_platforms_needed(weights, limit))
