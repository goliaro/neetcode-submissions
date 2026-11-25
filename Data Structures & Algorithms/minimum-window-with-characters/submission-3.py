from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # l inclusive, r exclusive
        # 1. initialize l as first useful character
        # 2. increment r until reaching valid window
        # 3. set min window size
        # while r<len(s):
        # increment r by 1, while still valid, increment l, update min
        if len(t) == 0 or len(s) < len(t):
            return ""
        match = dict(Counter(t))
        needed=match.copy()
        have={}
        l=0
        while l<len(s):
            if s[l] in match:
                break
            l+=1
        r=l
        while r<len(s) and len(needed)>0:
            if s[r] in needed:
                if needed[s[r]] == 1:
                    del needed[s[r]]
                else:
                    needed[s[r]] -= 1
            if s[r] in match:
                have[s[r]] = have.get(s[r],0)+1
            r+=1
        if len(needed)>0:
            return ""

        if (r-l) == len(t):
            return s[l:r]
        

        best_l, best_r = l,r
        while True: 
            while s[l] not in match or have[s[l]] > match[s[l]]:
                if s[l] in have:
                    have[s[l]] -= 1
                l+=1
            if (r-l) < (best_r - best_l):
                best_l, best_r = l,r
            if r < len(s):
                if s[r] in have:
                    have[s[r]] += 1
                r+=1
            else:
                break
            
        
        return s[best_l:best_r]
        


