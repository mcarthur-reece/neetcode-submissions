class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] *26
        i = 0
        while i < len(s) or i < len(t):
            if i < len(s):
                freq[ord(s[i])- ord('a')] += 1
            if i < len(t):
                freq[ord(t[i])- ord('a')] -= 1
            i += 1
        for val in freq:
            if val != 0:
                return False
        return True