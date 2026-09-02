class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ''.join([x.lower() for x in s if x.isalnum()])

        for i in range((len(words) + 1)//2):
            if words[i] != words[len(words)-(i+1)]:
                return False
        return True