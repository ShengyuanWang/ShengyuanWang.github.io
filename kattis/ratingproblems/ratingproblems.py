def main():
    a, b  = map(int, input().strip() .split())
    nums_high = [3]*a
    nums_low = [-3]*a
    for i in range(b):
        t = int(input())
        nums_high[i] = t
        nums_low[i] = t
    ans1 = sum(nums_low) / a
    ans2 = sum(nums_high) / a
    print(ans1, ans2)

if __name__ == "__main__":
    main()
     
