# https://leetcode.com/problems/add-digits/description/

def add_digits(num: int) -> int:
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


num = 555
print(add_digits(num))
