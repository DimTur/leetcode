# https://leetcode.com/problems/valid-anagram/description/

def is_anagram(s: str, t: str) -> bool:
    str_1 = sorted(s)
    str_2 = sorted(t)

    if str_1 == str_2:
        return True
    else:
        return False


s1 = "anagram"
t1 = "nagaram"
s2 = "rat"
t2 = "car"

print(is_anagram(s1, t1))
print(is_anagram(s2, t2))
