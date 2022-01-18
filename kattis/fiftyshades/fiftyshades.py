nums = int(input())
res = 0
for i in range(nums):
    letters = input().lower()
    if "pink" in letters or "rose" in letters:
        res += 1
if res == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(res)