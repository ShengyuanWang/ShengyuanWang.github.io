n, q = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
dic = {}
for i in range(n):
    if nums[i] in dic:
        dic[nums[i]].append(i+1)
    else:
        dic[nums[i]] = [i+1]
for i in range(q):
    x, k = map(int, input().strip().split())
    if x in dic and len(dic[x]) >= k:
        print(dic[x][k-1])
    else:
        print(-1)

