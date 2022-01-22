
def solve(a, b):
    larger = max(a, b)
    return larger

def main():
    a, b = map(int, input().strip().split())
    a, b = int(str(a)[::-1]), int(str(b)[::-1])
    return solve(a, b)

if __name__ == "__main__":
    print(main())