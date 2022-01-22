def main():
    t = int(input())
    total  =0
    for i in range(t):
        number = input()
        num = int(number[:len(number)-1])
        power = int(number[-1])
        total += num ** power
    print(total)
    return

if __name__ == "__main__":
    main()

