from collections import defaultdict

def are_isomorphic_strings(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    if s=="" and t=="":
        return True

    s_to_t = defaultdict(int)
    t_to_s = defaultdict(int)
    for i in range(len(s)):
        if s_to_t[s[i]] == 0:
            if t_to_s[t[i]] == 0:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            else:
                if t_to_s[t[i]] != s[i]:
                    return False
        else:
            if s_to_t[s[i]] != t[i]:
                return False
    
    return True