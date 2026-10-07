
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freqs1={}
        for c in s1:
            freqs1[c]=freqs1.get(c,0)+1
        
        used={}
        start=0
        # iterate through s2, for each char, if encounter some char not in cur
        for i,c in enumerate(s2):
            if c not in freqs1:
                used={}
                continue
            if len(used)==0:
                start=i
            used[c]=used.get(c,0)+1
            if used[c]>freqs1[c]:
                # need to move start until we find another c
                while start<i:
                    if s2[start]==c:
                        used[c]-=1
                        start+=1
                        break
                    else:
                        used[s2[start]]-=1
                        start+=1
            if i-start==len(s1)-1:
                return True
        return False

            