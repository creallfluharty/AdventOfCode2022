with open("input.txt") as f:
    sol = 0
    cycle = 1
    X = 1
    for line in f:
        op, *nums = line.rstrip().split()
        if op == 'noop':
            takes, nX = 1, X
        else:
            takes, nX = 2, X + int(nums[0])

        for i in range(takes):
            if cycle % 40 == 20:
                sol += cycle * X

            cycle += 1

        X = nX

print(sol)
