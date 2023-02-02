from typing import List

def get_maximum_profit_brute_force(prices: List[int]) -> int:
    maximum_profit = 0

    # i = buy day
    for i in range(0, len(prices)-1):
        # j = sell day
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit

def get_maximum_profit_sliding_window(prices: List[int]) -> int:
    if len(prices) < 2: return 0
    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

