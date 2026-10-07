class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        start=0
        unique_chars=set()
        for end in range(len(s)):
            new_c=s[end]
            end+=1

            if new_c not in unique_chars:
                unique_chars.add(new_c)
                longest=max(longest,end-start)
                continue
            else:
                # increment start and remove each character until you get to new_c
                while start<end:
                    old_c=s[start]
                    start+=1
                    if old_c ==new_c:
                        break
                    else:
                        unique_chars.remove(old_c)

            # print(f"end={end}, start={start}, s[end]={s[end]}, len(unique_chars)={len(unique_chars)}, longest={longest}")
            # if s[end] not in unique_chars:
            #     unique_chars.add(s[end])
            # end+=1
            #     longest=max(longest,end-start)
            #     print(f"\tend={end}, longest={longest}")
            # else:
            #     while start<end:
            #         c_remove = s[start]
            #         unique_chars.remove(c_remove)
            #         start+=1
            #         print(f"\tc_remove={c_remove}, start={start}")
            #         if c_remove == s[end]:
            #             break
        return longest