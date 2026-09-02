class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        words = ''.join([x for x in s if x.isalpha()| x.isalnum()])

        for i in range((len(words) + 1)//2):
            if words[i] != words[len(words)-(i+1)]:
                return False
        return True