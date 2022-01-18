t = int(input())
for i in range(t):
    w, g, h, r = map(int, input().strip().split())

    maxh = ((h+g-r-r)**2 + w**2)**0.5
    minh = ((abs(g-h))**2 + w**2)**0.5
    print(round(minh,6), round(maxh, 6))