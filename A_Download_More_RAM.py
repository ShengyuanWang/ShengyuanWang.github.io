t = int(input())

    



for i in range(t):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    dict = {}
    for i in range(n):
        if a[i] in dict:
            dict[a[i]].append(b[i])
        else:
            dict[a[i]] = [b[i]]
    dict = sorted(dict)
    for num in dict:
        if num <= k:
            lst = dict[num]
            k += sum(lst)
    print(k)



