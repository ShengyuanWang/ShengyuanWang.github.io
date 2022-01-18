n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
maxNum = max(lst)
flag = True
for i in range(1, maxNum+1):
    if i not in lst:
        flag = False
        print(i)
if flag:
    print("good job")