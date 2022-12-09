with open("input.txt") as f:
    s = 0
    for line in f:
        half = len(line) // 2
        wrong, = set(line[:half]).intersection(line[half:])
        s += (ord(wrong) - ord('A') + 27) if wrong.isupper() else (ord(wrong) - ord('a') + 1)

    print(s)
