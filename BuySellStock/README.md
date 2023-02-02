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

#### Approach 1 (Brute Force)
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

#### Approach 2: Greedy method
- Moving through each element and pretend we sell it on the date we are at.
- At the same time, keep track of the "lowest price AT THE MOMENT" from the beginning to the selling date.
- Change lowest_price as needed, then calculate the maximum profit based on the lowest price.
- Example: 7 1 5 3 6 4
    - Sell date is day 0 (technically we cannot do this, but we will get 0 for maximum profit anyway because we don't buy or sell on the same day), lowest_price is 7. profit = prices[0] - lowest_price = 0.
    - Sell date is day 1. The price is 1. It's lower than the current lowest price => lowest_price = 1. profit = prices[1] - 1 = 0.
    - Sell date is day 2. The price is 4. It's higher than the current lowest price so lowest_price doesnt change. profit = prices[2] - 1 = 5 - 1 = 4 > current max_profit (0) => max_profit = 4.
    - Sell date is day 3. The price is 3. It's higher than the current lowest price so lowest_price doesnt change. profit = prices[3] - 1 = 3 - 1 = 2 < current max_profit.
    - Sell date is day 4. The price is 6. It's higher than the current lowest price so lowest_price doesnt change. profit = prices[4] - 1 = 6 - 1 = 5 > current max_profit => max_profit = 5.
    - Sell date is day 5. The price is 4. It's higher than the current lowest price so lowest_price doesnt change. profit = prices[5] - 1 = 4 - 1 = 3 < current max_profit.
    - Return max_profit = 5

### Pseudocode
#### Approach 1 (Brute Force)
- if array has less than 2 elements, return 0.
- Initialize variables:
    - A variable (type int) all max_profit to keep track of the max profit after all combination has been calculated. max_profit = 0
- Loop through all the day we can buy (from 0-> N-1)
    - Loop through all the day we can sell if we buy the stock at day i (from i+1 -> N-1)
        - profit = prices[j] - prices[i]
        - if profit > max_profit:
            max_profit = profit
- return max_profit

#### Approach 2: Greedy method
- if array has less than 2 elements, return 0.
- Initialize variables:
    - max_profit = 0
    - min_price = prices[0]
- Go through all the prices
    - if price < min_price:
        - min_price = price
    - profit = price - min_price
    - if profit > max_profit
        max_profit = profit

### BigO
#### Approach 1 (Brute Force)
- For each day we buy, we test it with all the day we can sell. There are N days we can choose to buy, for each day we can choose N-1 day to sell => O(N^2).
- Space complexity: only use profit to keep track of current profit => O(1)

#### Approach 2: Greedy method
- We go through each price once => O(N)
- Only keep track of min_price and profit => space complexity O(1)

