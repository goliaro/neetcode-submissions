from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0 or len(s)<len(t):
            return ""
        match = Counter(t)
        window = Counter()
        
        need = len(match)

        l=0
        best_l, best_r = 0, len(s)+1
        for r in range(len(s)):
            if s[r] in match:
                window[s[r]] = window.get(s[r],0)+1
                if window[s[r]] == match[s[r]]:
                    need -= 1
            while need == 0:
                if (r-l) < (best_r - best_l):
                    best_l, best_r = l,r
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < match[s[l]]:
                        need=1
                l+=1
        if best_r == len(s)+1:
            return ""
        else:
            return s[best_l:best_r+1]
            
            