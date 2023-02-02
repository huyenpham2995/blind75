from collections import defaultdict 

def longest_palindrome(s: str) -> int:
    if len(s) < 1: return len(s)

    count = defaultdict(int)
    longest_palindrome = 0

    for letter in s:
        count[letter] += 1
        
    max_odd = 0
    longest_palindrome = 0
    for _, counts in count.items():
        if counts % 2 == 0:
            longest_palindrome += counts 
        else:
            longest_palindrome += counts -1 
            if counts > max_odd:
                max_odd = counts
         
    return longest_palindrome + 1 if max_odd > 0 else longest_palindrome