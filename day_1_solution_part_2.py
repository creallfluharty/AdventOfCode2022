import heapq

with open("day_1_input.txt") as f:
    cal_heap = []
    elf_cals = 0
    for line in f:
        if len(line.rstrip()) == 0:
            heapq.heappush(cal_heap, elf_cals)
            if len(cal_heap) > 3:
                heapq.heappop(cal_heap)
            elf_cals = 0
            continue

        elf_cals += int(line)

print(sum(cal_heap))