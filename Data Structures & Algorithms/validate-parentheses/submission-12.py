class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(" : ")",
                    "{" : "}",
                    "[" : "]"}

        open_brac = []
        

        for i in range(len(s)):
            if s[i] in brackets.keys():
                open_brac.append(s[i])
            elif len(open_brac) != 0:
                if s[i] == brackets[open_brac[-1]]:
                    open_brac.pop()
                else: 
                    return False
            else:
                return False
                
        if len(open_brac) != 0:
            return False
        else:
            return True
                

        