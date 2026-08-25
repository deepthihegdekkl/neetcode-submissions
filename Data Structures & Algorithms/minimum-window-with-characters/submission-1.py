class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq = {}
        freq1 = {}

        # Frequency of characters required from t
        for ch in t:
            freq[ch] = freq.get(ch, 0) + 1

        left = 0
        right = 0
        count = 0

        mini = float("inf")
        ans = ""

        while right < len(s):

            # Add current character to window
            ch = s[right]

            if ch in freq:
                freq1[ch] = freq1.get(ch, 0) + 1

                # We only count up to the required frequency
                if freq1[ch] <= freq[ch]:
                    count += 1

            # Window contains all characters of t
            while count == len(t):

                # Save the smallest window
                if right - left + 1 < mini:
                    mini = right - left + 1
                    ans = s[left:right + 1]

                # Remove left character
                left_ch = s[left]

                if left_ch in freq:
                    if freq1[left_ch] <= freq[left_ch]:
                        count -= 1

                    freq1[left_ch] -= 1

                left += 1

            # Expand window
            right += 1

        return ans