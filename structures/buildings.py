

def sarea(H, stack, i):
    j = stack.pop()
    t = stack[-1] + 1 if stack else 0
    return H[j] * (i - t)


def max_rectangular_area(H):
    stack = []
    max_area = 0

    for i, h in enumerate(H):
        if not stack or h >= H[stack[-1]]:
            stack.append(i)
            continue
        while stack and h < H[stack[-1]]:
            area = sarea(H, stack, i)
            max_area = max(max_area, area)
        stack.append(i)

    i += 1
    while stack:
        area = sarea(H, stack, i)
        max_area = max(max_area, area)

    return max_area


if __name__ == '__main__':
    print(max_rectangular_area([2, 1, 2, 3, 1]))
