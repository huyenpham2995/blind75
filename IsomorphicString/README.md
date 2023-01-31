### Question
- Given two strings s and t, determine if they are isomorphic.
- Two strings s and t are isomorphic if the characters in s can be replaced to get t.
- All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
- Example: 
    - Input: s = "egg", t = "add"
    - Output: true, since e->a, g->d in order.
[Link to question.](https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1)

### Thoughts
- Input and output:
    - Input: 2 strings - s and t
    - Output: True or False (are the isomorphic or not).
- What if the 2 strings are empty "": then it's True.
- Will there be special characters $*#$& or numbers in it? Assuming only letters for now, although it's not really different (maybe...).
- If the 2 strings' length are different, clearly they are not isomorphic.
- Think of this as a dictionary where 1 letter is equivalent to another.
    - Valid example: s="egg", t="add"
        - look at the first letter of s and t (e-a). So e is equivalent to a. Noted that.
        - Move on to the next one: g and d. So d is equivalent to d. Noted that.
        - Move on to the next letter: g and d. In the previous round, we note g is equivalen to d, and we see it's another pair of g-d => valid.
        - Nothing else to check. return true.
    - Invalid example: s="foo", t="bar"
        - Look at the first letter of both words: f and b. So f is equivalent to b. Noted that.
        - Move to the 2nd letter of both words: o and a. So o is equivalent to a. Noted that.
        - Move to the 2rd letter of both words: o and r. In the previous round, we already determined o is equivalent to a, but this is o and r instead. So these words are not isomorphic.
- Can make use of dictionary for this problem, where the key is the letter from word s, the value is the letter from word t. When the letter does not have a match, the value will be 0 (not yet matched). If there are already a letter matches to the current letter, then those 2 words are not isomorphic.
- Tricky case: when the letter in t already exists in s but it doesn't catch it. 
    - Example: s="badc", t="baba".
        - b matches with b.
        - a matches with a.
        - d matches with b. But b is already matches with b so invalid.
    - Need one more case: if the current letter of word t is already in the dictionary and matches with a value, check to see if that value is equal to the current letter at s. If it's not, they are not isomorphic.

Update:
- Apparently needs to keep track of t as well. So consider s as the word and t as the pattern. the pattern t has to match string s.
- Example: "paper" and :"title". 
    - p matches t, it repeats twice.
    - e matches l.
    - r matches e. And it is okay, it's one way matching, as long as the pattern (2 p repeatedly, 2 t repeatedly matches at the right place).
- The solution will change. 
    - 2 dictinaries to keep track of string s and t. 1 keeps track of the letter matching from s to t, the other keeps track of the letter matching t to s.
    - Looping through both string and record the match from s_to_t and t_to_s.

### Pseudocode
- If 2 strings are not the same length: return False.
- if 2 strings are both empty: return True.
- Initialize variable(s):
    - A dictionary to store the letter mapping from s to t, and another for t to s
- Loop through string s:
    - If the current letter of s is not in s_to_t:
        - If current letter of t is not in t_to_s: update both dictionaries.
        - If current letter of t is in t_to_s: see if it's the current letter of s. If it's not, that means 2 letters of s are mapped to the same letter of t => invalid.
    - If the letter of s is in s_to_t. Check to see if it is the current letter of t. If it's not, then that means 1 letter of s is mapped to 2 different letters of t => invalid.
    - If the loop can reach to the end, they are isomorphic.

### BigO
We loop through both string 1 time, so runtime would be O(2N) => O(N), with N being the length of both strings.