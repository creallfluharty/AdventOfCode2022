with open("input.txt") as f:
    cmd_res = ([line for line in cr.split('\n') if line] for cr in f.read().split('$ ') if cr)
    dir_sizes = []

    # Assuming every directory is visited exactly once
    def sol():
        size = 0
        while True:
            try:
                cmd, *res = next(cmd_res)
            except StopIteration:
                dir_sizes.append(size)
                return size

            if cmd.startswith('cd '):
                to = cmd[3:]
                if to == '..':
                    dir_sizes.append(size)
                    return size

                child_size = sol()
                size += child_size

            else: # ls
                for line in res:
                    if line.startswith('dir'):
                        continue  # as long as we never cd into a dir that doesn't exist, this information is redundant

                    s, name = line.split()
                    size += int(s)

    used = sol()
    need_to_free = used - 40000000  # 30000000 - (70000000 - used)
    print(min(size for size in dir_sizes if size >= need_to_free))