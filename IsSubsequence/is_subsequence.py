def is_subsequence(s, t):
    if s == "":
        return True

    index_s = 0
    index_t = 0

    while index_s < len(s) and index_t < len(t):
        if s[index_s] == t[index_t]:
            index_s += 1
        index_t += 1
    
    if index_s != len(s):
        return False
    return True
