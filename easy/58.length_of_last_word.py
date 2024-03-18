# https://leetcode.com/problems/length-of-last-word/description/

def length_of_last_word(s: str) -> int:
    new_s = s.split()
    word_len = len(new_s[-1])

    return word_len


# s = "Hello World"
# s = "   fly me   to   the moon  "
s = "luffy is still joyboy"

length_of_last_word(s)
