class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[c.lower() for c in s if c.isalnum()]
        return l == list(reversed(l))