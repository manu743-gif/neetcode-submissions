class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        l = 0
        c =0
        for r in range(len(s)):
            while s[r] in x:
                x.remove(s[l])
                l+=1
            x.add(s[r])
            c = max(c,r-l+1)
        return c