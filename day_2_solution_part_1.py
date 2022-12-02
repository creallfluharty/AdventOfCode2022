with open("day_2_input.txt") as f:
    score = 0
    for line in f:
        opponent, response = line.rstrip().split()
        opponent = ord(opponent) - ord('A')
        response = ord(response) - ord('X')

        if opponent == response:
            score += 3
        elif opponent == (response - 1) % 3:
            score += 6

        score += response + 1

    print(score)
