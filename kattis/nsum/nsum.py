def addition(nums):
    return sum(nums)

def main():
    t = int(input())
    nums = list(map(int, input().strip().split()))

    return addition(nums)




if __name__ == "__main__":
    print(main())