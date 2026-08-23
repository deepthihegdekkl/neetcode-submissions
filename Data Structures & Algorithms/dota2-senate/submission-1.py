from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()
        d = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        n = len(senate)

        while r and d:
            ri = r.popleft()
            di = d.popleft()

            if ri < di:
                # R gets to act first
                r.append(ri + n)
            else:
                # D gets to act first
                d.append(di + n)

        if r:
            return "Radiant"
        else:
            return "Dire"