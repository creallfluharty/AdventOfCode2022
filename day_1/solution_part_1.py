with open("day_1_input.txt") as f:
    max_cals = 0
    elf_cals = 0
    for line in f:
        if len(line.rstrip()) == 0:
            max_cals = max(max_cals, elf_cals)
            elf_cals = 0
            continue

        elf_cals += int(line)

print(max_cals)