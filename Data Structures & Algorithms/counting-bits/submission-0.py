class Solution:
    def countBits(self, n: int) -> List[int]:
        x = []
        for i in range(n+1):
            a = bin(i).count("1")
            x.append(a)
        return x