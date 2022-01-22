def main():
    x = int(input())
    n = int(input())
    used = 0
    for i in range(n):
        used += int(input())
    total = x*(n+1)
    print(total - used)
    return

if __name__ == "__main__":
    main()