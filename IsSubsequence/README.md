### Question
- Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
- A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
[Link to question.](https://leetcode.com/problems/is-subsequence/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: 2 strings s and t.
    - Output: a boolean if s is a subsequence of t.
- Questions:
    - Can we assume the length of s is always shorter or equal than that t? Yes because we are checking to see s is the subsequence of t.
    - Can both be empty string ""?
        - Yes. And in that case function will return True.
        - If s="" and t is not empty, s is still the subsequence of t.
    - Do we differentiate between lowercases and uppercases? No, only lowercases. No special character.
- s is always shorter than t. So we can check in t to see if it has all the letters of s in order. If we go through all the letter of t but we don't see all the letters of s in order, then s is not a subsequence of t. If all the letter of s in order is included in t, then s is a subsequence of t.
- Example 1: s="abc", t="ahbgdc'
    - First look at the first letter of s: a. Go through t. First letter of t is a, we move on to the 2nd letter of s.
    - 2nd letter of s is b. Next letter of t is h. No match.
    - 2nd letter of s is b. Next letter of t is b. Match. Move on.
    - 3rd letter of s is c. Next letter of t is g. No match.
    - 3rd letter of s is c. Next letter of t is d. No match.
    - 3rd letter of s is c. Next letter of t is c. Match.
    - Reach the end of s, the end of t => s is a subsequence of t.
- Example 2: s="axc", t="ahbghdc"
    - First look at the first letter of s: a. Go through t. First letter of t is a, we move on to the 2nd letter of s.
    - 2nd letter of s is x. Next letter of t is h. No match.
    - 2nd letter of s is x. Next letter of t is b. No match.
    - 2nd letter of s is x. Next letter of t is g. No match.
    - 2nd letter of s is x. Next letter of t is h. No match.
    - 2nd letter of s is x. Next letter of t is d. No match.
    - 2nd letter of s is x. Next letter of t is c. No match.
    - Reach the end of t but not the end of s => s is not a subsequence of t.

### Pseudocode
- Check to see if s is empty or both string is empty, return True.
- Initialize variables:
    - index_s = 0 to keep track of letter position of s.
    - index_t = 0 to keep track of letter position of t.
- Set up a loop, when index_s < len(s) and index_t < len(t):
    - If the current letter of s == the current letter of t: move up index_s.
    - Move up index_t
- Until the end, if index_s != len(s) (could not reach the end of s), then return False. Else True.

### BigO
- We will go through all the letters in s and t. Since t is longer or equal to s, then the time complexity is O(T), with T being length of string t.

