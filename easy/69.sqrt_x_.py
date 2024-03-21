# https://leetcode.com/problems/sqrtx/description/

def my_sqrt(x: int) -> int:
    left = 0
    right = x

    while right >= left:
        mid = left + (right - left) // 2

        if mid ** 2 > x:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1


# x = 4
x = 8
my_sqrt(x)
