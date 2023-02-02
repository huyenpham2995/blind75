### Question
- You are given an array prices where prices[i] is the price of a given stock on the ith day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
[Link to question.](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: array of integers, represents stock prices.
    - Output: the maximum value.
- We can sell before buying, so if we choose to buy from a certain day, you can only look at the price of the day afterwards.
- No same-day trade allowed either.
- This would be best represents by a table, with row as buying price and column as selling price. Example: prices = [7,1,5,3,6,4]
| Buy/Sell | 7 | 1  | 5  | 3  | 6  | 4  |
|----------|---|----|----|----|----|----|
| 7        | x | -6 | -2 | -4 | -1 | -3 |
| 1        | x | x  | 4  | 2  | 5  | 3  |
| 5        | x | x  | x  | -2 | 2  | -1 |
| 3        | x | x  | x  | x  | 3  | 1  |
| 6        | x | x  | x  | x  | x  | -2 |
| 4        | x | x  | x  | x  | x  | x  |

### Pseudocode


### BigO
