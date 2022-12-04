with open("input.txt") as f:
    s = 0
    while True:
        common = set(f.readline().rstrip()).intersection(f.readline().rstrip()).intersection(f.readline().rstrip())
        if len(common) == 0:
            break

        badge, = common
        s += (ord(badge) - ord('A') + 27) if badge.isupper() else (ord(badge) - ord('a') + 1)

    print(s)
