n = int(input())
def solve(n):
    if n == 2:
        print("NO")
        return
    if n % 2 == 0:
        print("YES")
        return
    print("NO")

solve(n)