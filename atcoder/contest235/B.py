
def solve(heights):
    temp = heights[0]
    for height in heights[1:]:
        if height > temp:
            temp = height
        else:
            print(temp)
            return 
    print(temp)
    return
t = int(input())
heights = list(map(int, input().split()))
solve(heights)

