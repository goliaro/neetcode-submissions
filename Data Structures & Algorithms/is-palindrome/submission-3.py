class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l=[c.lower() for c in s if c.isalnum()]

        left=0;right=len(s)-1
        while left<right:
            l=s[left].lower()
            r=s[right].lower()
            while not l.isalnum() and left < right:
                left+=1
                l=s[left].lower()
            while not r.isalnum() and left < right:
                right-=1
                r=s[right].lower()
            if left> right:
                return False
            if l != r:
                return False
            left+=1; right-=1
        return True