# https://leetcode.com/problems/valid-palindrome/description/

def is_palindrome(s: str) -> bool:
    s_lower = s.lower()
    s1 = "".join(c for c in s_lower if c.isalnum())
    s1_p = s1[::-1]

    if s1 == s1_p:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
is_palindrome(s)
