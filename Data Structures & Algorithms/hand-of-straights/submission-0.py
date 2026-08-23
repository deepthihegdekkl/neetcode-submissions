class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for num in hand:
            freq[num] = freq.get(num, 0) + 1

        for k in sorted(freq):
            if freq[k] == 0:
                continue

            if k - 1 not in freq or freq[k - 1] == 0:
                count = freq[k]

                for i in range(groupSize):
                    if freq.get(k + i, 0) < count:
                        return False

                    freq[k + i] -= count

        return True