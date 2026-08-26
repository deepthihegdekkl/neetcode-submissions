class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(s):
            l = len(s)

            if len1 % l != 0 or len2 % l != 0:
                return False

            f1 = len1 // l
            f2 = len2 // l

            return s * f1 == str1 and s * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(str1[:l]):
                return str1[:l]

        return ""