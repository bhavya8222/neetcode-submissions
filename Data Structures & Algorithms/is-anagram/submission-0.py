class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            if s.count(ch) != t.count(ch):
                return False
        return True