def IoC(inp: str):
    inp = "".join(inp.strip().split()).upper()
    print(inp)
    count = {}
    for i in range(26):
        count[chr(ord("A")+i)] = 0
    for i in inp:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count[i] += 1
    prob = []
    for i in count.keys():
        if count[i]:
            prob.append(count[i]/ len(inp))

    tot = sum(prob)/ len(prob)
    return tot

