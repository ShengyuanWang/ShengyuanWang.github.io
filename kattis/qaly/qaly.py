num = int(input())
res = 0
for i in range(num):
    lst = list(map(float, input().strip().split()))
    res += lst[0]*lst[1]
print(res)