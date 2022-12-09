with open("input.txt") as f:
    cmd_res = ([line for line in cr.split('\n') if line] for cr in f.read().split('$ ') if cr)

# Assuming every directory is visited exactly once
def sol():
    size = 0
    small_children_size = 0
    for cmd, *res in cmd_res:
        if cmd.startswith('cd '):
            to = cmd[3:]
            if to == '..':
                return small_children_size, size

            small_grandchildren_size, child_size = sol()
            size += child_size
            small_children_size += small_grandchildren_size
            if child_size < 100_000:
                small_children_size += child_size

        else: # ls
            for line in res:
                if line.startswith('dir'):
                    continue  # as long as we never cd into a dir that doesn't exist, this information is redundant

                s, name = line.split()
                size += int(s)

    return small_children_size, size

print(sol()[0])