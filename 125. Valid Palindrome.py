class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =''.join(e for e in s if e.isalnum())

        if s.lower() == s[::-1].lower():
            return True