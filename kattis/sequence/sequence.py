MOD = 10**9+7
MEM = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

def mod_pow2(n):
    while n >= len(MEM):
        MEM.append((MEM[-1] * 2) % MOD)
    return MEM[n]

def inversions(bstr):
    total, zeros, questions = (0,)*3
    for x in reversed(bstr):
        if x == '1':
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % MOD
        elif x == '0':
            zeros += 1
        else:
            total *= 2
            z = zeros * mod_pow2(questions)
            q = 0 if questions == 0 else questions * mod_pow2(questions-1)
            total = (total + z + q) % MOD
            questions += 1

    return total

def main():
    print(inversions(input()))

if __name__ == "__main__":
    main()