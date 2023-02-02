### Question
- You are given an array prices where prices[i] is the price of a given stock on the ith day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
[Link to question.](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: array of integers, represents stock prices.
    - Output: the maximum value.
- Can this array be empty? yes. Return 0, no transaction.
- Can this array only has 1 value? yes. return 0 since no transaction.
- We can sell before buying, so if we choose to buy from a certain day, you can only look at the price of the day afterwards.
- No same-day trade allowed either.
- We can try to buy the stock at 1 day, then sell it at all the other day after that. For each day we choose to buy the stock, we try to sell it at all the day after the day we buy and see which combo generate the best benefit.
- This would be best represents by a table, with row as buying price and column as selling price. Example: prices = [7,1,5,3,6,4]

| Buy/Sell | 7 | 1  | 5  | 3  | 6  | 4  |
|----------|---|----|----|----|----|----|
| 7        | x | -6 | -2 | -4 | -1 | -3 |
| 1        | x | x  | 4  | 2  | 5  | 3  |
| 5        | x | x  | x  | -2 | 2  | -1 |
| 3        | x | x  | x  | x  | 3  | 1  |
| 6        | x | x  | x  | x  | x  | -2 |
| 4        | x | x  | x  | x  | x  | x  |

- For all day that the date of buy is larger than or equal to the date of sell, it is invalid (cannot buy after selling or on the day of selling) => arr[i][j] = x, or we don't need to care about it.
- For other day, the profit is calculated by taking the price of selling - the price of buying.
    - Buy at day 0, sell at day 1: arr[1] - arr[0] = 1 - 7 = -6.
    - Buy at day 4, sell at day 5: arr[5] - arr[4] = 4 - 6 = -2.
    - Generally, arr[i][j] = prices[j] - arr[i] for i from 0->5, j from i+1 -> 5.

### Pseudocode
- if array has less than 2 elements, return 0.
- Initialize variables:
    - A variable (type int) all max_profit to keep track of the max profit after all combination has been calculated. max_profit = 0
- Loop through all the day we can buy (from 0-> N-1)
    - Loop through all the day we can sell if we buy the stock at day i (from i+1 -> N-1)
        - profit = prices[j] - prices[i]
        - if profit > max_profit:
            max_profit = profit
- return max_profit

### BigO
- For each day we buy, we test it with all the day we can sell. There are N days we can choose to buy, for each day we can choose N-1 day to sell => O(N^2).
