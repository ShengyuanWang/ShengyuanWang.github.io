class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings) // 2
        dic = {}
        cnt = 0
        for i in range(n):
            pos = rings[i*2+1]
            color = rings[i*2]
            if pos in dic:
                if color not in dic[pos]:
                    dic[pos].append(color)
            else:
                dic[pos] = []
                dic[pos].append(color)
        for pos in dic:
            if len(dic[pos]) == 3:
                cnt += 1
        return cnt 


