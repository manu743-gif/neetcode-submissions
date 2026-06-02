class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        l = 0
        maxlen = 0

        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[l])
                l += 1

            a.add(s[right])
            maxlen = max(maxlen, right - l + 1)

        return maxlen