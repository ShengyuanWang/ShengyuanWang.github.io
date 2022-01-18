nums = int(input())
notes = list(input().strip().split())
total = 0
for note in notes:
    if len(note) == 1:
        total += 2
    else:
        total += (int(note[1])+1)
total -= 1

dic = {}
dic["G"] = [" " for _ in range(total)]
dic["F"] = ["-" for _ in range(total)]
dic["E"] = [" " for _ in range(total)]
dic["D"] = ["-" for _ in range(total)]
dic["C"] = [" " for _ in range(total)]
dic["B"] = ["-" for _ in range(total)]
dic["A"] = [" " for _ in range(total)]
dic["g"] = ["-" for _ in range(total)]
dic["f"] = [" " for _ in range(total)]
dic["e"] = ["-" for _ in range(total)]
dic["d"] = [" " for _ in range(total)]
dic["c"] = [" " for _ in range(total)]
dic["b"] = [" " for _ in range(total)]
dic["a"] = ["-" for _ in range(total)]

tmp = 0
for note in notes:
    if len(note) == 1:
        dic[note][tmp] = "*"
        tmp += 2
    else:
        letter = note[0]
        t = int(note[1])
        for i in range(t):
            dic[letter][tmp+i] = "*"
        tmp += (1+t)
for i in ["G", "F", "E", "D", "C", "B", "A", "g", "f", "e", "d", "c", "b", "a"]:
    res = ""
    res += f"{i}: "
    for j in dic[i]:
        res += j
    print(res)


