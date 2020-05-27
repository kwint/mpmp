# https://www.youtube.com/watch?v=ILrqPpLpwpE
solutions = []
for i in range(1, 10000):
    for j in range(1, 10000):
        tr = [i, i+j]
        while tr[-1] < 1000000:
            tr.append(tr[-2] + tr[-1])
        if tr[-1] == 1000000:
            print(f"started with {i} and {j} and took {len(tr)}")
            solutions.append([i, j, len(tr)])
