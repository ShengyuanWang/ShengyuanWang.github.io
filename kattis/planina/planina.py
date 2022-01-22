def main():
    times = [2]
    for i in range(15):
        times.append(times[-1]*2-1)
    t = int(input())
    side = times[t]
    ans = side * side
    print(ans)
    return

if __name__ == "__main__":
    main()
