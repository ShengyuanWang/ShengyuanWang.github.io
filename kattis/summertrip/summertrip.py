s = input()
n = len(s)

res = 0
for start in range(n-1):
    if s[start] == s[start+1]:
        continue
    lst = []
    for end in range(start+1, n):
        if s[start] == s[end]:
            break
        if s[end] in lst:
            continue
        res += 1
        if s[end] not in lst:
            lst.append(s[end])

print(res)