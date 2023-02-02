### Question
- Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
- Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
[Link to question.](https://leetcode.com/problems/longest-palindrome/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: a string
    - Output: the length of the longest palindrome (int).
- Letters are case sensitive, so A != a.
- If the length of the string is less than 2, then return the length of it.
    - "" has 0 palindrome.
    - "a" has 1 palindrome, which is a.
- The question said: using the letters in the string to build the longest palindrome. So we can move the letters around.
- We ony need the length of the palindrome, so we don't really need to construct the string.
- Cases of palindrome:
    - The 2 special cases ("" and 1 letter is covered in the original case).
    - "aaa": 1 letter appears an odd number of times.
    - "bb", "baab": any even number of letters combined with each other will make palindrome
    - "baaab", "bbabb": all even occurences of letters + only 1 odd occurence of a single letter.
- We can go through the string and count the occurence of each letter.
    - Any letter appears an even number of time, it can be in the palindrome.
    - Keep track of the letter with the max odd occurences in the string. Add that to the previous number. If there's no letter that occurs even amount of times, then this is actually the length of the longest palindrome.
- TRICK!!!!!!!!
    - We are NOT only taking the count of the letter that have the maximum odd occurence. For all letters that have odd occurence, we can make a palindrome with an even occurence of that letter. 
        - Example: "baaacccb", we can take 2 a and 2 c, and later add 1 more (either a or c) to the palindrome.
    - So, the fomular should be:
        - Count all even occurence
        - For odd occurence, take the # of occurence - 1
        - At the end, if there's any odd occurencce of a letter, add 1 to the final result (since we are allowed to have 1 letter with odd occurence, and in previous rounds we -1 for all odd occurence).

### Pseudocode
- if len(s) < 2 return len(s).
- Create a dictionary to count the occurence of each letter in the string.
- Afterwards, add the number of even occurences.
- If the number is odd, add number -1 to the final result.
- If there's an odd occurence, +1 to the final result
- Return final result.

### BigO
- Create a dictionary take O(N) time. Go through each entries in there again take at most O(N) time => time complexity O(N).
- At most we store N letters and their count in the dictionary => space complexity O(N).
