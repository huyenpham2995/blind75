from typing import List

def get_maximum_profit(prices: List[int]) -> int:
    maximum_profit = 0

    # i = buy day
    for i in range(0, len(prices)-1):
        # j = sell day
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit

