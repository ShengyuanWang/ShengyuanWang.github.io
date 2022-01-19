class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        res = []
        if n % k != 0:
            require = k * (n//k) + k - n
            for _ in range(require):
                s += fill
        for i in range(len(s)//k):
            ans = s[i*k:(i+1)*k]
            res.append(ans)
        return res