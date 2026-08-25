class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        mini=prices[0]
        for i in range(len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            maxi=max(maxi,prices[i]-mini)
        return maxi
        
        