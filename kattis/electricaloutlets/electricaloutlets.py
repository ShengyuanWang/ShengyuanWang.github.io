num = int(input())
for i in range(num):
    lst = list(map(int, input().strip().split()))
    strips = lst[0]
    total = 0
    for i in range(1, strips+1):
        total += lst[i]
    total -= (strips - 1)
    print(total)