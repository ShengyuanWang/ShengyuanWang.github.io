def main():
    a = int(input())
    b = int(input())
    if a >0 and b > 0:
        ans = 1
    elif a > 0 and b < 0:
        ans = 4
    elif a < 0 and b > 0:
        ans = 2
    else:
        ans = 3
    print(ans)
    return

if __name__ == "__main__":
    main()