with open("input.txt") as f:
    buffer = [['.' for _ in range(40)] for _ in range(6)]
    cycle = 1
    X = 1
    for line in f:
        op, *nums = line.rstrip().split()
        if op == 'noop':
            takes, nX = 1, X
        else:
            takes, nX = 2, X + int(nums[0])

        for i in range(takes):
            y, x = divmod(cycle - 1, 40)

            if X - 1 <= x <= X + 1:
                buffer[y][x] = '#'

            cycle += 1

        X = nX

print('\n'.join(''.join(row) for row in buffer))
