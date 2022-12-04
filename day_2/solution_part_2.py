with open("day_2_input.txt") as f:
    score = 0
    for line in f:
        opponent, action = line.rstrip().split()
        opponent = ord(opponent) - ord('A')
        action = ord(action) - ord('X')

        if action == 0:  # need to lose
            response = (opponent - 1) % 3
        elif action == 1:  # need to draw
            score += 3
            response = opponent
        else:  # need to win
            score += 6
            response = (opponent + 1) % 3

        score += response + 1

    print(score)