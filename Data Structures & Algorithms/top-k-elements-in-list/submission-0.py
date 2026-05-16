class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = Counter(nums)
        ss = sorted(s.items(), key=lambda x: x[1], reverse=True)
        l = []
        for i in range(k):
            l.append(ss[i][0])
        return l
