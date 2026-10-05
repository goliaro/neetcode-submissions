class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_prices=[]
        for i, price in enumerate(prices):
            # add min so far to the buying prices
            if i==0:
                buying_prices.append(price)
            else:
                buying_prices.append(min(buying_prices[-1], price))
        max_profit=0
        for i, price in enumerate(prices):
            max_profit=max(max_profit, price-buying_prices[i])
        return max_profit