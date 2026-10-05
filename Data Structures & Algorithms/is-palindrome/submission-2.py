class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[c.lower() for c in s if c.isalnum()]

        left=0;right=len(l)-1
        while left<right:
            if l[left] != l[right]:
                return False
            left+=1; right-=1
        return True