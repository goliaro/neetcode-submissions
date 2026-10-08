class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for p in s:
            if p == "(" or p == "[" or p == "{":
                stack.append(p)
            else:
                if p == ")":
                    if len(stack)==0 or stack[-1] != "(":
                        return False
                    else:
                        stack.pop()
                elif p == "]":
                    if len(stack)==0 or stack[-1] != "[":
                        return False
                    else:
                        stack.pop()
                else:
                    if len(stack)==0 or stack[-1] != "{":
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0
                