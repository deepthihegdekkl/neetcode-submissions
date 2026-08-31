class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    

        if len(hand) % groupSize != 0:
            return False

        frequency = {}

        for num in hand:
            frequency[num] = frequency.get(num, 0) + 1

        for num in sorted(frequency):

            while frequency[num] > 0:

                current = num
                groupsize = groupSize

                while groupsize > 0:

                    if frequency.get(current, 0) == 0:
                        return False

                    frequency[current] -= 1
                    current += 1
                    groupsize -= 1

        return True