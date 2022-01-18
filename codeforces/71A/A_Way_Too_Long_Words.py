t = int(input())


def solve(word):
    n = len(word)
    if n > 10:
        begin = word[0]
        end = word[-1]
        res = begin + str(n-2) + end
        print(res)
        return
    else:
        print(word)
        return

for i in range(t):
    word = input()
    solve(word)
