class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        total = 0
        while maxDoubles > 0 and target != 1:
            if target % 2 != 0:
                target -= 1
                total += 1
            else:
                target /= 2
                maxDoubles -= 1
                total += 1
        total += (target - 1)
        return int(total)