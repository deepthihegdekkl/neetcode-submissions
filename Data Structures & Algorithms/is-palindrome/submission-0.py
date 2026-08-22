class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for ch in s:
            if ch.isalnum():
                rev+=ch.lower()
        if rev==rev[::-1]:
            return True
        else:
            return False

        